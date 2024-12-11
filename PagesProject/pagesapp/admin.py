from django.contrib import admin
from .models import Post, Author

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', )
    date_hierarchy = 'created_at'
