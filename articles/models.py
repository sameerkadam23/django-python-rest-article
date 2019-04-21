from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    author = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
    