# breakeven/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.breakeven_analysis, name='breakeven_analysis'),
]
