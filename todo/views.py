from django.shortcuts import render

from todo.models import Todo
 

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"todo_list": todos})

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/todo_detail.html', {'todo': todo})