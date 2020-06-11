from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, UpdateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
    template_name = "article_list.html"
    model = Article
    
class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article

class ArticleUpdateView(UpdateView):
    template_name = "article_edit.html"
    fields = ('title', 'body')
    model = Article
    
class ArticleDeleteView(DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy('article_list') 