from django.urls import path
from. import views


urlpatterns = [
    # Otras rutas aquí...
  
    path('inicio/', views.inicio, name='inicio'),
    path('insertar_usuario/', views.insertar_usuario, name='insertar_usuario'),
    path('mostrar_usuario/', views.mostrar_usuario, name='mostrar_usuario'),
    path('login/', views.login, name='login'),
    path('insertar_juego/', views.insertar_juego, name='insertar_juego'),
    path('mostrar_juego/', views.mostrar_juego, name='mostrar_juego'),
    path('insertar_pelicula/', views.insertar_pelicula, name='insertar_pelicula'),
    path('mostrar_pelicula/', views.mostrar_pelicula, name='mostrar_pelicula'),
    path('insertar_capitulo/', views.insertar_capitulo, name='insertar_capitulo'),
    path('mostrar_capitulo/', views.mostrar_capitulo, name='mostrar_capitulo'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('calculadora_para_invitados/', views.calculadora_para_invitados, name='calculadora_para_invitados'),
    path('salva/', views.salva, name='salva'),
    path('cargar_archivo/', views.cargar_archivo, name='cargar_archivo'),
    path('cargar_archivo_usuario/', views.cargar_archivo_usuario, name='cargar_archivo_usuario'),
    path('envio_correo/', views.envio_correo, name='envio_correo'),
    path('insertar_web/', views.insertar_web, name='insertar_web'),
    path('mostrar_web/', views.mostrar_web, name='mostrar_web'),
    path('mostrar_web_invitados/', views.mostrar_web_invitados, name='mostrar_web_invitados'),












 



]