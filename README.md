# Gestor-de-Tareas
Aplicación web en Python que permita a los usuarios gestionar sus tareas diarias.

## Funcionalidades
- Agregar nuevas tareas con nombre y descripción.
- Marcar tareas como completadas usando un checklist.
- Eliminar tareas específicas.
- Exportar tareas a un archivo JSON.
- Importar tareas desde un archivo JSON.

## Cómo ejecutar
1. Instalar las dependencias usando: pip install flask flask_sqlalchemy
2. Ejecutar la aplicación con: python app.py
3. Abrir en el navegador: http://127.0.0.1:5000/

## Estructura del Proyecto
- `app.py`: Archivo principal con la lógica de la aplicación.
- `templates/index.html`: Plantilla HTML para la interfaz.
- `static/css/styles.css`: Estilos para la aplicación.

## Base de Datos
La aplicación usa SQLite para almacenar las tareas. 
