from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    awards = models.TextField()
    site = models.URLField(null=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
