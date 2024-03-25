from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "app_aula/home.html")

def autores(request):
    return render(request, "app_aula/autores.html")

def fotos(request):
    return render(request, "app_aula/fotos.html")