from django import forms
from .models import UserInfo, TaskInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = TaskInfo
        fields = ('user_info',)