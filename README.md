# Proyecto Urban Grocers

Cessna Lara, Sprint 8, grupo 38 QA  

Descripción del Proyecto

Este proyecto automatiza las pruebas para la funcionalidad de creación de kits personalizados en Urban Grocers. El flujo de trabajo incluye:

1\. Creación de usuario: Generación de un nuevo perfil de usuario/a

2\. Autenticación: Obtención del token de autorización (authToken)

3\. Creación de kit: Asignación de un kit personalizado vinculado al usuario

El proyecto incluye 9 casos de prueba para el parámetro `name` al crear un kit:

5 pruebas positivas: Verifican que la creación del kit sea exitosa

4 pruebas negativas: Verifican el manejo correcto de errores (código 400)

Archivos del Proyecto

-Configuration.py: URLs y configuración del servidor

-data.py: Cuerpos de solicitud y datos de prueba

-sender\_stand\_request.py: Funciones para envío de solicitudes HTTP

-create\_kit\_name\_kit\_test.py: Casos de prueba automatizados

-README.md: Documentación del proyecto

-.gitignore: Archivos excluidos del control de versiones



Requisitos Previos


Antes de ejecutar las pruebas, asegúrate de tener instalados:

pytest

requests

El comando para ejecutar el proyecto
pytest folder/archivo.py.


Programas utilizados

postman para hacer pruebas previas

Pycharm

Gitbash

Github
