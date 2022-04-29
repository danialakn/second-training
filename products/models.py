from django.db import models

# Create your models here.
class products(models.Model):
    title   =models.CharField(max_length=30)
    price   =models.IntegerField()
    email   =models.EmailField(max_length=254)
