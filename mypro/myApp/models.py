from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=100)
    branch =models.CharField(max_length=100)
    college =models.CharField(max_length=100)
    grade =models.CharField(max_length=100)
