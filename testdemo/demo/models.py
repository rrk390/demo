from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    short_id = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

class TaskInfo(models.Model):
    user_info =  models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    coding = models.BooleanField(default=False)
    testing = models.BooleanField(default=False)
    req_analysis = models.BooleanField(default=False)

