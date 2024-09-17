from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'tasks':tasks,'form':form}
    return render(request, 'todoapp/index.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')