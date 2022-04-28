from django.db import models

# Create your models here.
# ブログの投稿のmodel
class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " _ " + self.title

# ブログのタスクのmodel

class Task(models.Model):

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " _ " + self.title
