from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='bl-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('video/', views.video, name='bl-video'),
    path('groups/', views.groups, name='bl-groups'),
    path('logout/', views.logout_view, name='logout'),
]
