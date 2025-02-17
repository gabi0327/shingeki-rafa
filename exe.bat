@echo off
cd /d "C:\Users\Killua\Documents\Shingeki Rafa Calculadora de Precio"

:: Ejecutar makemigrations y migrate
call python manage.py makemigrations
call python manage.py migrate

:: Iniciar el servidor Django en segundo plano
start cmd /k python manage.py runserver > nul

:: Esperar unos segundos para asegurarse de que el servidor esté listo
timeout /t 5

:: Abrir el navegador por defecto con la URL del servidor local
start "" %SystemRoot%\System32\cmd.exe /c start http://127.0.0.1:8000/

:: Mantener la ventana de comandos abierta
pause