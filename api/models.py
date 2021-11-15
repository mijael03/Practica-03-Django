from django.db import models

# Create your models here.
class Prestamo(models.Model):
    libro=models.IntegerField()
    usuario=models.IntegerField()
    fecprestamo=models.DateField()
    fecdevolucion=models.DateField()
    