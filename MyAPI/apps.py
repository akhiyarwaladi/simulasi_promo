from django.apps import AppConfig
import joblib

class MyapiConfig(AppConfig):
	name = 'MyAPI'
	regr_1 = joblib.load('/home/akhiyarwaladi/gli/gli_prelim/model/regr_1.sav')
	regr_2 = joblib.load('/home/akhiyarwaladi/gli/gli_prelim/model/regr_2.sav')
