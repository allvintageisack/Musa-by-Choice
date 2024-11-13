from django.db import models

class Drivers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)


