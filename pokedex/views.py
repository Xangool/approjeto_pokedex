from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def listarPokemons (request):
    pokemon = Pokemon.objects.all()

    contexto = {
        "todos_pokemons" : pokemon
    }

    return render(request,'listar.html', contexto)