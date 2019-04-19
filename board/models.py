from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateField()
    counts = models.IntegerField()

# Create your models here.
