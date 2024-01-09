# todo_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'action': 'Create'})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'action': 'Update'})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo_list')
