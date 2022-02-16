from curses.ascii import US
from dataclasses import fields
from pyexpat import model
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['vehiclename', 'vehicleowner', 'password']
        widgets ={
            'vehiclename':forms.TextInput(attrs={'class':'form-control'}),
            'vehicleowner':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }