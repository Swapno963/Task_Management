from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription= models.TextField()
    is_completed = models.BooleanField()
    taskDate = models.DateField( auto_now=False, auto_now_add=False)
    category = models.ManyToManyField(CategoryModel)


    def __str__(self) -> str:
        return f'{self.taskTitle}-{self.is_completed}'