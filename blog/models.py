from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='images/')
    autor = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()
    video_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
