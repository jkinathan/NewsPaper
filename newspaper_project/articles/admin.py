from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class CommentInline(admin.TabularInline): # new can also use StackedInline
    model = Comment
    
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]
    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)

