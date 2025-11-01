from django.urls import path
from . import views

urlpatterns = [
    path('', views.meme_create, name='meme_create'),
    path('meme/<int:pk>/', views.meme_detail, name='meme_detail'),
    path('edit/<int:pk>/', views.meme_edit, name='meme_edit'),
]
