from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    short_link = models.CharField(max_length=16)
    title = models.TextField()
    content = models.TextField()