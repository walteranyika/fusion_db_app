from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'category', 'cost', 'price', 'for_sale', 'pic']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # help_texts = {
        #     'password1': '',
        #     'password2': '',
        # }
