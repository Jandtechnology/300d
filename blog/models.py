from django.db import models

# Create your models here.
class project(models.Model): # Con esta Clase llamada proyect creo una tabla
    name = models.CharField(max_length=50) #Esta es tu primera columna. 