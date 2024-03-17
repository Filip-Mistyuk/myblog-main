from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
