from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)