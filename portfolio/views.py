from django.shortcuts import render
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {
        'projects': projects
    })
