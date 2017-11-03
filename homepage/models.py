# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500, default="Default Title Post")
    link = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    source = models.CharField(max_length=50)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " -- " + self.author
