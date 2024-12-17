from django.shortcuts import render , redirect
from .models import Todo
# Create your views here.
def home(request):
    data = Todo.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        create = Todo.objects.create(task = task , description = description)
    context = {'data':data}
    return render(request,'home.html',context)

def alltodos(request):
    data1 = Todo.objects.all()
    context = {
        'data' : data1
    }
    return render(request,'alltodos.html',context)

def todolists(request,pk):
    data2 = Todo.objects.get(id = pk)
    context = {
        'data' : data2
    }
    return render(request,'todolists.html',context)

def edit(request,pk):
    data3 = Todo.objects.get(id=pk)
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        data3.task = task
        data3.description = description
        data3.save()
        return redirect('alltodos')
    
    context = {
        'data' : data3
    }
    return render(request,'edit.html',context)