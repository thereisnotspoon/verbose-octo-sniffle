from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy

# Create your views here.

def index(request):
    A = ['hola', 'mudo', 'hello', 'word']
    template = loader.get_template('signos/index.html')
    context = {
        'clave1' : 'valor1',
        'clave2' : 'valor2',
        'clave3' : 'valor3',
        'clave4' : 'valor4',
        'clave5' : 'valor5',
	'A' : A,
    }
    return HttpResponse(template.render(context, request))
