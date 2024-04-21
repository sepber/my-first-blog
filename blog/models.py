from django.conf import settings
from django.db import models
from django.utils import timezone

# https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
# Create your models here.
# Create an Object named Post
# (models.Model) means that Post is a Django model
class Post(models.Model):
    # link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # define text with a limited number of chars
    title = models.CharField(max_length=200)
    # define unlimited text
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title