from django import forms

class ApprovalForm(forms.Form):
	period=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Berapa lama promo berlangsung (dalam hari)'}))
	min_purchase_qty=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Jumlah pembelian minimum produk'}))
	disc_amount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Jumlah diskon yang diberikan (dalam rupiah)'}))
	is_multiple_apply=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Apakah promo bisa di apply berulang?'}))
	wom=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Minggu ke berapa promo akan dimulai?'}))
	#firstname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
	#lastname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
	#Dependents=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents'}))
	#ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
	#CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income'}))
	#LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount'}))
	#Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan Term in Months'}))
	#Credit_History=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Last Credit Rating'}))
	#Credit_History=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
	#Gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
	#Married=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
	#Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not_Graduate', 'Not_Graduate')])
	#Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
	#Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')])
