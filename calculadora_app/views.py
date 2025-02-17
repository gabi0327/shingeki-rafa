# Create your views here.
from django.shortcuts import render



def mostrar_web_invitados(request):
    return render(request,'mostrar_web_invitados.html')








def mostrar_web(request):
    return render(request,'mostrar_web.html')






def insertar_web(request):
    return render(request,'insertar_web.html')





def envio_correo(request):
    return render(request,'envio_correo.html')






def cargar_archivo_usuario(request):
    return render(request,'cargar_archivo_usuario.html')






def cargar_archivo(request):
    return render(request,'cargar_archivo.html')






def salva(request):
    return render(request,'salva.html')





def calculadora_para_invitados(request):
    return render(request,'calculadora_para_invitados.html')


def calculadora(request):
    return render(request,'calculadora.html')



def mostrar_capitulo(request):
    return render(request,'mostrar_capitulo.html')


def insertar_capitulo(request):
    return render(request,'insertar_capitulo.html')


def mostrar_pelicula(request):
    return render(request,'mostrar_pelicula.html')


def insertar_pelicula(request):
    return render(request,'insertar_pelicula.html')






def mostrar_juego(request):
    return render(request,'mostrar_juego.html')


def insertar_juego(request):
    return render(request,'insertar_juego.html')




def login(request):
    return render(request,'login.html')



def mostrar_usuario(request):
    return render(request,'mostrar_usuario.html')


def insertar_usuario(request):
    return render(request,'insertar_usuario.html')


def inicio(request):
    return render(request,'inicio.html')


