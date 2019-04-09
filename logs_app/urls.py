"""Defines URL patterns for logs_app"""

from django.urls import path

from . import views

app_name = 'logs_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<str:topic_name>/', views.topic, name="topic"),
    path('new-topic/', views.new_topic, name='new_topic'),

]