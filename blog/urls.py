from django.urls import path
from .views import BlogListView,BlogDetailView, BlogAbout

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', BlogAbout.as_view(), name='about'),
]
