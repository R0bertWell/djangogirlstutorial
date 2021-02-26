from django.contrib import admin
from .models import Post


@admin.register(Post)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
