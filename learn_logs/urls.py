"""Defines URL patterns for learn_logs."""

from django.urls import path
from . import views


app_name = 'learn_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'), 
]
