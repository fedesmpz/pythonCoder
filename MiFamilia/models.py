from django.db import models

# Create your models here.
class Familiar(models.Model):
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    email = models.EmailField()
