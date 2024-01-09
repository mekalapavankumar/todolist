# todo_app/urls.py
from django.urls import path
from .views import todo_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]
