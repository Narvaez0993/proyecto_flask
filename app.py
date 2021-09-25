from logging import debug
from flask import Flask, request, redirect
from flask.templating import render_template
app = Flask(__name__)

tareas = []

@app.route("/")
def home():
    return render_template("index.html",tareas = tareas)

@app.route("/agregar", methods=["GET","POST"])
def agregar():
    if request.method == "GET":
        return render_template("agregar.html")
    else:
        tarea = request.form.get("comida")
        tareas.append(tarea)
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

