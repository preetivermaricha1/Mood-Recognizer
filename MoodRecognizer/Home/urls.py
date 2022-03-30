from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='Home'),
    path('mainpage/', views.mainpage, name='Home'),
    path('mainpage/mycode/', views.mycode, name='Home'),
    
]