from django.db import models


# Create your models here.

class Marcas(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Presentacion(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Registros(models.Model):
    marca = models.ForeignKey(Marcas,on_delete=models.CASCADE)
    presentacion = models.ForeignKey(Presentacion,on_delete=models.CASCADE)

    def get_marca(self):
        return self.marca

    def get_presentacion(self):
        return self.presentacion
