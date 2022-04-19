from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('price/', views.price, name='price'),
    path('price', views.price, name='price'),
    path('home/', views.home, name='home'),
    
]