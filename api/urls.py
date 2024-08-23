from django.urls import path
from .views import user_list, user_detail, user_create

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('users/create/', user_create, name='user_create'),
]