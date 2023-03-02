from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField()
    rating = models.IntegerField()
    year = models.DateField()
    category = models.ManyToOneRel()
