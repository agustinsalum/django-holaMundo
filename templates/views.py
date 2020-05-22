from django.shortcuts import render

# Create your views here.


def holaMundo (request):
    nombre = 'Agustin'
    dicci = {'nombre' : nombre}
    return render (request, 'proyectoApp/holaMundo.html', dicci)
