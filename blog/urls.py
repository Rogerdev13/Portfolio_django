from django.urls import path
from .views import render_posts , post_unique

app_name = 'blog'

urlpatterns = [
    path('' , render_posts , name='posts'),
    path('<int:post_id>' , post_unique , name='post_unique')
]