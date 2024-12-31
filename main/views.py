from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        todo_name = request.POST.get('name')
        temp = Todo.objects.create(title=todo_name)
        if temp:
            messages.success(request, "Todo added successfully")
            return render(request, 'main/home.html',context={'todos':todos})
        else:
            messages.error(request, "Something went wrong")
            return render(request, 'main/home.html',context={'todos':todos})
    
    return render(request, 'main/home.html', context={'todos':todos})

def done(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = True
    todo.save()
    messages.success(request, "Todo done successfully")
    return redirect("/")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, "Todo deleted successfully")
    return redirect("/")