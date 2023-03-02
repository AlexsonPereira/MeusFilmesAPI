import uuid
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid, primary_key=True, editable=False)
    name = models.CharField()
