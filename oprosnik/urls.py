from django.contrib import admin
from django.urls import path, include

import oprosnik

from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('login/', views.login, name='login'),
    # poll
    path('poll/', views.PollView.as_view({'get': 'list', 'post': 'create'})),
    path('poll/<int:pk>/', views.PollView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('poll/active/', views.ActivePollView.as_view({'get': 'list'})),
    # question
    path('question/', views.QuestionView.as_view({'get': 'list', 'post': 'create'})),
    path('question/<int:pk>/', views.QuestionView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # choice
    path('choice/', views.ChoiceView.as_view({'get': 'list', 'post': 'create'})),
    path('choice/<int:pk>/', views.ChoiceView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # answer
    path('answer/', views.AnswerView.as_view({'get': 'list', 'post': 'create'})),
    path('answer/<int:pk>/', views.AnswerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]
