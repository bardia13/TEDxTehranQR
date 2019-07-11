from django.db import models

# Create your models here.


class Dare(models.Model):
    token = models.CharField(max_length=4)
    count = models.IntegerField(default=0)
