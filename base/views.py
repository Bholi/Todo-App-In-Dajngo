from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def home(request):
    todo = Todo.objects.all()
    return render(request, 'index.html',{'todo':todo})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        Todo.objects.create(name = name, description = desc, status = status)
        return redirect('home')

    return render(request, 'create.html')

def edit(request,pk):
    edit_todo = Todo.objects.get(id = pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        edit_todo.name = name
        edit_todo.description = desc
        edit_todo.status = status
        edit_todo.save()
        return redirect('home')
    return render(request, 'edit.html',{'todo':edit_todo})

def delete(request,pk):
    delete_todo = Todo.objects.get(id = pk)
    delete_todo.delete()
    return redirect('home')
    


