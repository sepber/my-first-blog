from django.contrib import admin
from .models import Post

# Register your models here.
# make model Post visible on the admin page
admin.site.register(Post)