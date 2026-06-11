from django.urls import path
from blogs.views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('blog/', blog_list, name='blog_list'),
    path('add-blog/', blog_add, name='blog_add'),
    path('edit-blog/<str:b_id>/', blog_edit, name='blog_edit'),
    path('delete/<str:b_id>/', blog_delete, name='blog_delete'),
]
