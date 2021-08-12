from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):

    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'главная страница сайта', 'tasks': tasks})


def contact(request):
    return render(request, 'main/contact.html')


def reg(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('two')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/reg.html', context)


def service(request):
    return render(request, 'main/service.html')


def uslugi(request):
    return render(request, 'main/uslugi.html')


def anti(request):
    return render(request, 'main/anti.html')


def uslug1(request):
    return render(request, 'main/uslug1.html')


def uslug2(request):
    return render(request, 'main/uslug2.html')


def uslug3(request):
    return render(request, 'main/uslug3.html')


def uslug4(request):
    return render(request, 'main/uslug4.html')


def uslug5(request):
    return render(request, 'main/uslug5.html')

def otdel(request):
    return render(request, 'main/otdel.html')
def voprose(request):
    return render(request, 'main/voprose.html')


