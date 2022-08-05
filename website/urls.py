
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('services.html', views.services, name="services"),
]

