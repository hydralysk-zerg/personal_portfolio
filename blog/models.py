from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date_post = models.DateField(auto_created=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    