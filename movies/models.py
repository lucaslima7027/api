from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=500)
    synopsis = models.CharField(max_length=5000)
    duration = models.IntegerField()
    poster = models.FilePathField()
    director = models.ManyToManyField("Director")

    def __str__(self):
        return self.name
    


class Director(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    nationality = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
# Create your models here.
