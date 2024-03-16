from django import forms

from .models import Mess_minutes
from .models import Registration_Request
from .models import Semdates


class MinuteForm(forms.ModelForm):
    class Meta:
        model = Mess_minutes
        fields = ('meeting_date', 'mess_minutes')

class MessInfoForm(forms.Form, ):
    MESS_CHOICES= [
        ('mess1', 'Veg Mess'),
        ('mess2', 'Non Veg Mess'),
        ]
    mess_option = forms.CharField(label='Mess Option', widget=forms.Select(
        choices=MESS_CHOICES, attrs={'style': 'border-radius:1rem;padding:7px;'}))



class RegistrationRequest(forms.ModelForm):
    end_date = Semdates.objects.latest('start_date')
    class Meta:
        model = Registration_Request
        fields = ('Txn_no','amount','img','start_date','payment_date')  
        
        widgets={
            'Txn_no':forms.TextInput(attrs={'class':'ui big input','style':'border-radius:4px', 'initial':'590'}),
            'amount':forms.TextInput(attrs={'class':'ui big input'}),
            'img':forms.FileInput(attrs={'class':'ui big input'}),
            'start_date':forms.widgets.DateInput(attrs={'type':'date'}),
            'payment_date':forms.widgets.DateInput(attrs={'type':'date'}),
        }  
