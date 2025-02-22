from django.db import models
from django.utils.text import slugify

from accounts.models import User
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


# Create your models here.
class Post(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='author')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='static/images/posts/', null=True, blank=True)
    keywords = models.CharField(null=True, blank=True, verbose_name='separated with comma (,)')
    created = models.DateTimeField(auto_now_add=True)
    is_hot_post = models.BooleanField(default=False, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.created)

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})
