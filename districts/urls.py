from django.urls import path
from districts import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]