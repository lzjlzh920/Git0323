
from django.db import models

# Create your models here.
class Area(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self',null=True,blank=True)
