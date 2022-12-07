from django.db import models


# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    #date=models.DateTimeField()
    #type=models.CharField(max_length=10, choices= Type_Content ,null=False, blank=False)