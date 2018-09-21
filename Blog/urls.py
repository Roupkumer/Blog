from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_post, name='list_post'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.new_post, name='new_post'),
]
