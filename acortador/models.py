from django.db import models
from django import forms

# Create your models here.
class URLs(models.Model):
    larga = models.CharField(max_length = 100)

class NameForm(forms.Form):
    url = forms.CharField(label='url', max_length=100)
