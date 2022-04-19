from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    date_created =  models.DateTimeField()

    def __str__(self):
        return self.title
