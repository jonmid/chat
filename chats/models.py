from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description