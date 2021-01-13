from django.shortcuts import render,redirect
from myApp.models import Emp
from myApp.forms import EmpForm

def display(request):
    e = Emp.objects.order_by('eno')
    d = {'emp':e}
    return render(request,'myApp/index.html',d)

def insert(request):
    f = EmpForm()
    if request.method=="POST":
        f = EmpForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d = {'form':f}
    return render(request,'myApp/insert.html',d)

def delete(request,id):
    e = Emp.objects.get(id=id)
    e.delete()
    return redirect('/')

def update(request,id):
    e = Emp.objects.get(id=id)
    if request.method=="POST":
        f = EmpForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d = {'emp':e}
    return render(request,'myApp/update.html',d)
