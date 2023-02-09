from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    return render(request, 'ai_posts/index.html', {'title': 'Главная', 'categories': categories})


def contacts(request):
    return render(request, 'ai_posts/contacts.html', {'title': 'Контакты'})


def mailing(request):
    return render(request, 'ai_posts/mailing.html', {'title': 'Рассылка'})


def about(request):
    return render(request, 'ai_posts/about.html', {'title': 'О нас'})


def categories(request):
    cats = Category.objects.all()
    return render(request, 'ai_posts/categories.html', {'categories': cats})


def all_posts(request, cat_id):
    category = Category.objects.filter(pk=cat_id)[0]
    posts = Post.objects.filter(post_category_id=cat_id)
    return render(request, 'ai_posts/all_posts.html', {'category': category, 'posts': posts})
