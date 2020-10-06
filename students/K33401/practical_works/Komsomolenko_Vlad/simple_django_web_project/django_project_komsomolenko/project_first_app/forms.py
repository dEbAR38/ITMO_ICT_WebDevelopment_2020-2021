from django import forms
from .models import Owner


class addOwner(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "birthdate",
        ]