from datetime import date
from django import forms
from django.core import validators
from django.core.validators import RegexValidator
# creating a form 
import re

from django.forms.widgets import TextInput



class InputForm(forms.Form):
    pred=forms.CharField(label='Test Input', validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")]
    ,max_length=150, widget=forms.Textarea(attrs={'class':"form-control"}))

    def clean_pred(self):
         data= self.cleaned_data.get('pred')
         dig='[^0-9]'

         valid= re.match(data, dig)
         if not valid:
             raise forms.ValidationError('check your input')

         return data