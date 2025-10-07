from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits= 6 ,decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="books/")

def __str__(self):
    return self.title
