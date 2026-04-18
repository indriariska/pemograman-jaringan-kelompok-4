from django.shortcuts import render
from .models import Project


def home(request):
    latest_projects = Project.objects.order_by('-id')[:6]

    return render(request, 'home.html', {
        'projects': latest_projects
    })


def about(request):
    return render(request, 'about.html')


def project_list(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': projects
    })


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')