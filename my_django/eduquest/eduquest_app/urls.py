from django.urls import path
from eduquest_app import views

urlpatterns = [
    path('', views.index, name='index'),
]