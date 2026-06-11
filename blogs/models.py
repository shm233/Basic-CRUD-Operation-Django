from django.db import models

# Create your models here.

class BlogModel(models.Model):
    CAT = [
        ('Educational', 'Educational'),
        ('Technologies', 'Technologies'),
        ('Sports', 'Sports')
    ]
    title = models.CharField(max_length=255, null=True)
    author_name = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    category = models.CharField(max_length=20, choices=CAT, null=True)
    blog_image = models.ImageField(upload_to='media/blog', null=True)
    publish_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.title}---{self.author_name}"
