from django.db import models
class Articolo(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()

# Create your models here.
