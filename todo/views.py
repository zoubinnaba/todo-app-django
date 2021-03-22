from django.shortcuts import render, redirect

from todo.models import Todo
from todo.forms import TodoForm
 

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"todo_list": todos})

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # create the todo object
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect('/')
    return render(request, 'todo/todo_create.html', {'form': form})
    