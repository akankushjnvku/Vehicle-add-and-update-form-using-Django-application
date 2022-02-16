from django.db import models

# Create your models here.
class User(models.Model):
    vehiclename=models.CharField(max_length=70)
    vehicleowner=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
