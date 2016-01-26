# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(
		max_length = 100,label="",
		widget=forms.TextInput(attrs={'placeholder': 'Contact Name','class': 'form-control','autofocus':'','required':''})
	)
    contact_email = forms.EmailField(
		max_length = 225,label="",
		widget=forms.TextInput(attrs={'placeholder': 'Contact Email','class': 'form-control','required':'','type':'email'})
	)