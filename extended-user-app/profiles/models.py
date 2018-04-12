from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.TextField(max_length=50, blank=True)
    bio = models.CharField(max_length=1000, blank=True)