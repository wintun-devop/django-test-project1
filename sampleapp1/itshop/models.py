from django.db import models

# Create your models here.
"""
Create model for brands and categories.After model creation,import this models to
admin.py and make register on there.

"""

class Brand(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name