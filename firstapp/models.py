from django.db import models

# Create your models here.
class BlogPosts(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    contents=models.TextField()
    published=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.FileField(blank=True)
    objects=models.Manager()