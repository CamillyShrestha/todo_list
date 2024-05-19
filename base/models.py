from django.db import models
from django.contrib.auth.models import User #This handles authentication for username, pw
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    create = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self) -> str: #This is used for string representaion whenver print() or str() function is called this method is called
        return self.title


    class Meta: 
        ordering = ['complete']
    