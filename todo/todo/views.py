from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todo.models import TODOO
from django.shortcuts import get_object_or_404


def home(request):
    if request.user.is_authenticated:
        return redirect('todo')
    return redirect('signup')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('fnm')
        email = request.POST.get('emailid')
        password = request.POST.get('pwd')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('loginn')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('fnm')
        password = request.POST.get('pwd')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo')
        else:
            return render(request, 'loginn.html', {'error': 'Invalid credentials'})

    return render(request, 'loginn.html')


@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TODOO.objects.create(title=title, user=request.user)
        return redirect('todo')

    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


@login_required(login_url='login')
def delete_todo(request, srno):
    TODOO.objects.get(srno=srno, user=request.user).delete()
    return redirect('todo')


@login_required(login_url='login')
def edit_todo(request, srno):
    obj = TODOO.objects.get(srno=srno, user=request.user)

    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.save()
        return redirect('todo')

    return render(request, 'edit_todo.html', {'obj': obj})


def signout(request):
    logout(request)
    return redirect('loginn')



@login_required(login_url='login')
def toggle_status(request, srno):
    todo = get_object_or_404(TODOO, srno=srno, user=request.user)
    todo.status = not todo.status
    todo.save()
    return redirect('todo')

