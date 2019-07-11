from django import forms

from MainApp.models import *

class ProductForm(forms.ModelForm):
    class Meta():
         model=Product
         fields='__all__'

class CartForm(forms.ModelForm):
    class Meta():
        model=Cart
        fields=['count']