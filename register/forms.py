from django import forms

class RegistForm(forms.Form):
	a = forms.CharField()
	b = forms.CharField()