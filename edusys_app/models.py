from django.db import models
from django.contrib.auth.models import User

class University(models.Model):
    id = models.DecimalField()
    full_name_university = models.CharField(max_length=200)
    short_name_university = models.CharField(max_length=200)

