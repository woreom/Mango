

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import Profile


# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField(required=False)

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=1000, required=False, help_text='Optional.')
    gender = forms.ChoiceField( choices=(("M","M"),("F","F")), required=False, help_text='Optional.',)
    class Meta:
        model = Profile
        fields = ('bio', 'gender')


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class SignUpForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    ####help_text='Required. Inform a valid email address.'
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
