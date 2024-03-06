from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import never_cache

from Student.models import Student

@never_cache
def home(request):
    return render(request,'home.html')

@login_required
@never_cache
def display(request):
    students = Student.objects.all()
    data = {'students': students}
    return render(request,'display.html',data)

@login_required
@never_cache
def addstudent(request):
    if request.method == 'GET':
        return render(request, 'addstudent.html')
    else:
        student = Student()
        student.Name = request.POST['tbname']
        student.Age = request.POST['tbage']
        student.City = request.POST['tbcity']
        student.Email = request.POST['tbemail']
        student.Phone = request.POST['tbphone']
        student.save()
        return redirect('displaystudents')

@login_required
@never_cache
def editstudent(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        data = {'student':student}
        return render(request, 'editstudent.html', data)

    else:
        student.Name = request.POST['tbname']
        student.Age = request.POST['tbage']
        student.City = request.POST['tbcity']
        student.Email = request.POST['tbemail']
        student.Phone = request.POST['tbphone']
        student.save()
        return redirect('displaystudents')

@login_required
@never_cache
def deletestudent(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('displaystudents')

@never_cache
def login_fun(request):
    if request.method == 'GET':
        return render(request, "login.html")

    else:
        uname = request.POST["tbusername"]
        pword = request.POST["tbpass1"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            request.session['name'] = user.username
            return redirect("home")
        else:
            return redirect("login")

@never_cache
def register_fun(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        p1 = request.POST["tbpass1"]
        p2 = request.POST["tbpass2"]
        un = request.POST["tbusername"]
        em = request.POST["tbemail"]
        if p1 == p2:
            u = User.objects.create_superuser(un, em, p1)
            u.save()
            return redirect("login")
        else:
            return redirect('register')


def logout_fun(request):
    del request.session['name']
    logout(request)
    return redirect("login")