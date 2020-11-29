from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm
from . apps import MyapiConfig
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter


class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers

def rupiah_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]
    before_decimal = before_decimal[0:2]
    return "Rp " + temp_result + "," + before_decimal

def ohevalue(df):
	ohe_col=joblib.load("/home/akhiyarwaladi/gli/example/DjangoBootStrap/MyAPI/allcol.pkl")
	cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	newdf=pd.DataFrame(newdict)
	return newdf

def approvereject(unit):
	try:
		mdl=joblib.load("/home/akhiyarwaladi/gli/example/DjangoBootStrap/MyAPI/loan_model.pkl")
		scalers=joblib.load("/home/akhiyarwaladi/gli/example/DjangoBootStrap/MyAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])

def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				#Firstname = form.cleaned_data['firstname']
				#Lastname = form.cleaned_data['lastname']
				#Dependents = form.cleaned_data['Dependents']
				#ApplicantIncome = form.cleaned_data['ApplicantIncome']
				#CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
				#LoanAmount = form.cleaned_data['LoanAmount']
				#Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
				#Credit_History = form.cleaned_data['Credit_History']
				#Gender = form.cleaned_data['Gender']
				#Married = form.cleaned_data['Married']
				#Education = form.cleaned_data['Education']
				#Self_Employed = form.cleaned_data['Self_Employed']
				#Property_Area = form.cleaned_data['Property_Area']
				period = form.cleaned_data['period']
				min_purchase_qty = form.cleaned_data['min_purchase_qty']
				disc_amount = form.cleaned_data['disc_amount']
				is_multiple_apply = form.cleaned_data['is_multiple_apply']
				wom = form.cleaned_data['wom']
				myDict = (request.POST).dict()
				print(myDict)
				df=pd.DataFrame(myDict, index=[0])
				print(df)
				answer1 = MyapiConfig.regr_1.predict(df.iloc[:,1:])[0]
				print(answer1)
				answer1 = int(answer1)
				answer2 = MyapiConfig.regr_2.predict(df.iloc[:,1:])[0]
				print(answer2)
				answer2 = rupiah_format(answer2)
				
				#answer=approvereject(ohevalue(df))[0]
				#Xscalers=approvereject(ohevalue(df))[1]
				#if int(df['LoanAmount'])<25000:
				messages.success(request,'Perkiraan jumlah struk: \n{}\n\n\n Perkiraan sales: \n{}'.format(answer1, answer2))
				#else:
				#	messages.success(request,'Invalid: Your Loan Request Exceeds $25,000 Limit')
	
	form=ApprovalForm()
				
	return render(request, 'myform/cxform.html', {'form':form})

def cxcontact2(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				Firstname = form.cleaned_data['firstname']
				Lastname = form.cleaned_data['lastname']
				Dependents = form.cleaned_data['Dependents']
				ApplicantIncome = form.cleaned_data['ApplicantIncome']
				CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
				LoanAmount = form.cleaned_data['LoanAmount']
				Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
				Credit_History = form.cleaned_data['Credit_History']
				Gender = form.cleaned_data['Gender']
				Married = form.cleaned_data['Married']
				Education = form.cleaned_data['Education']
				Self_Employed = form.cleaned_data['Self_Employed']
				Property_Area = form.cleaned_data['Property_Area']
				myDict = (request.POST).dict()
				df=pd.DataFrame(myDict, index=[0])
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				messages.success(request,'Application Status: {}'.format(answer))
	
	form=ApprovalForm()
				
	return render(request, 'myform/form.html', {'form':form})



