import json
from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/alzat/OneDrive/Documentos/Gestion_Tareas/instance/GestionTareas.db'
db = SQLAlchemy(app)

import os
print("Ruta absoluta de la base de datos:", os.path.abspath("instance/GestionTareas.db"))

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    nueva_tarea = Tarea(nombre=nombre, descripcion=descripcion)
    db.session.add(nueva_tarea)
    db.session.commit()
    return redirect('/')

@app.route('/marcar_completada/<int:id>', methods=['POST'])
def marcar_completada(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.estado = not tarea.estado
    db.session.commit()
    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect('/')

@app.route('/exportar')
def exportar():
    tareas = Tarea.query.all()
    lista_tareas = [
        {"nombre": t.nombre, "descripcion": t.descripcion, "estado": t.estado}
        for t in tareas
    ]
    response = Response(json.dumps(lista_tareas, indent=4), mimetype="application/json")
    response.headers["Content-Disposition"] = "attachment; filename=tareas.json"
    return response

@app.route('/importar', methods=['POST'])
def importar():
    archivo = request.files.get("archivo")
    if archivo and archivo.filename.endswith(".json"):
        datos = json.load(archivo)
        for tarea in datos:
            nueva_tarea = Tarea(
                nombre=tarea["nombre"],
                descripcion=tarea["descripcion"],
                estado=tarea.get("estado", False)
            )
            db.session.add(nueva_tarea)
        db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        try:
            print("Intentando crear la base de datos...")
            db.create_all()  # Crea las tablas si no existen
            print("Base de datos creada correctamente.")
        except Exception as e:
            print("Error al crear la base de datos:", e)
        app.run(debug=True)
