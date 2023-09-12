from django.contrib import admin  
from django.urls import path 
from Exam import views
urlpatterns = [  
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),
    path('paymongo/', views.paymongo, name='paymongo'),
]