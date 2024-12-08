from tkinter.constants import CASCADE

from django.db import models
from django.forms import CharField


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="myfiles/photos/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name














