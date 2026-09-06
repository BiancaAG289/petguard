"""
main.py
--------
Archivo principal de PetGuard.

Por ahora este archivo SOLO arranca la aplicación Flask y define
las rutas necesarias para ver las páginas del MVP. Todavía no hay:
- base de datos
- login / registro funcional
- asistente de IA

Esas funciones se irán agregando en las siguientes etapas.
"""

from flask import Flask, render_template

app = Flask(__name__)

# Ruta de la página de inicio
@app.route("/")
def index():
    return render_template("index.html")

# Ruta de la página de login (todavía sin lógica de autenticación)
@app.route("/login")
def login():
    return render_template("login.html")

# Ruta de la página de registro de usuario (todavía sin lógica)
@app.route("/register")
def register():
    return render_template("register.html")

# Ruta del perfil de usuario (todavía sin datos reales)
@app.route("/profile")
def profile():
    return render_template("profile.html")

# Ruta del perfil de una mascota (todavía sin datos reales)
@app.route("/pet")
def pet():
    return render_template("pet.html")

# Ruta de la página del asistente (todavía sin conexión a IA)
@app.route("/assistant")
def assistant():
    return render_template("assistant.html")


if __name__ == "__main__":
    app.run(debug=True)
