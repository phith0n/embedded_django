import importlib
from django.db import models
from django.apps import AppConfig


class Collection(models.Model):
    name = models.CharField('name', max_length=128)
