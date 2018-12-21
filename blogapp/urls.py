from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]