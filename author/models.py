from django.db import models
from author.models import Author

# Create your models here.=

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    pseudonym = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

