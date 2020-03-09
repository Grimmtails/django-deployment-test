from django import forms
from django.contrib.auth.models import User
from FifthLvlApp.models import UserProInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class meta():
        model = User
        fields = ('username','email','password')

class UserProInfoForm(forms.ModelForm):
    class meta():
        model = UserProInfo
        fields = ('portfolio_site','profile_pic')