from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
    
    #path('', views.sayHello, name='sayHello'),
    #path('', views.index, name='index'),
    ]