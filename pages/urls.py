from django.urls import path
from . import views
urlpatterns = [
 path('', views.mainpage),
 path('login/', views.login),
 path('enroll/', views.enroll),
 path('about/', views.about),
 path('faq/', views.faq),
 path('service/', views.service),
 ]