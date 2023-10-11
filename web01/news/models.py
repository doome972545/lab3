from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    newscontent = models.TextField()
    def __str__(self) -> str:
        return self.title