from django.db import models

class member(models.Model): 
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    num=models.IntegerField(null=True)
    joining_date=models.DateField(null=True)
# Create your models here.
