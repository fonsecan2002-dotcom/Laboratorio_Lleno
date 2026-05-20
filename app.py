from flask import Flask, jsonify, request, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR)

# -----------------------------------
# ESTADO DEL LABORATORIO
# -----------------------------------
estado = {
    "capacidad_maxima": 5,
    "estudiantes": []
}

# -----------------------------------
# RUTAS ESTÁTICAS
# -----------------------------------
@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

# -----------------------------------
# API: OBTENER ESTADO
# -----------------------------------
@app.route("/api/estado", methods=["GET"])
def obtener_estado():
    return jsonify({
        "estudiantes": estado["estudiantes"],
        "cantidad": len(estado["estudiantes"]),
        "capacidad_maxima": estado["capacidad_maxima"],
        "disponible": len(estado["estudiantes"]) < estado["capacidad_maxima"]
    })

# -----------------------------------
# API: INGRESAR ESTUDIANTE
# -----------------------------------
@app.route("/api/ingresar", methods=["POST"])
def ingresar():
    datos = request.get_json()
    nombre = datos.get("nombre", "").strip()

    if not nombre:
        return jsonify({
            "exito": False,
            "mensaje": "Ingrese el nombre del estudiante."
        }), 400

    if len(estado["estudiantes"]) >= estado["capacidad_maxima"]:
        return jsonify({
            "exito": False,
            "mensaje": "El laboratorio está lleno."
        }), 400

    if nombre in estado["estudiantes"]:
        return jsonify({
            "exito": False,
            "mensaje": f'"{nombre}" ya está registrado en el laboratorio.'
        }), 400

    estado["estudiantes"].append(nombre)

    return jsonify({
        "exito": True,
        "mensaje": f"¡Bienvenido, {nombre}!",
        "estudiantes": estado["estudiantes"],
        "cantidad": len(estado["estudiantes"]),
        "disponible": len(estado["estudiantes"]) < estado["capacidad_maxima"]
    })

# -----------------------------------
# API: RETIRAR ESTUDIANTE
# -----------------------------------
@app.route("/api/salir", methods=["POST"])
def salir():
    datos = request.get_json()
    nombre = datos.get("nombre", "").strip()

    if not nombre:
        return jsonify({
            "exito": False,
            "mensaje": "Seleccione un estudiante para retirar."
        }), 400

    if nombre not in estado["estudiantes"]:
        return jsonify({
            "exito": False,
            "mensaje": f'"{nombre}" no se encuentra en el laboratorio.'
        }), 404

    estado["estudiantes"].remove(nombre)

    return jsonify({
        "exito": True,
        "mensaje": f"{nombre} salió del laboratorio.",
        "estudiantes": estado["estudiantes"],
        "cantidad": len(estado["estudiantes"]),
        "disponible": len(estado["estudiantes"]) < estado["capacidad_maxima"]
    })

# -----------------------------------
# EJECUTAR
# -----------------------------------
if __name__ == "__main__":
    print("\n✅ Servidor iniciado")
    print("🌐 Abrir en: http://localhost:5000\n")
    app.run(debug=True, port=5000)