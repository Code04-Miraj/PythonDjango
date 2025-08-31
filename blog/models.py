from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'), ('published' , 'Published'))

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    def save(self, *args , **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args , **kwargs)


    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


    def __str__(self):
        return self.title        




