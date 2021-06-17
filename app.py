from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "Universidad": "UTPL",
        "Curso": "Procesos de Ingeniería de Software",
        "Alumno": "Bruno Alexander Esparza Carchi",
        "Período": "Abr/Ago 2021",
        "Lenguaje de programación preferido": "Javascript",
        "Aspiración PostGraduación": "Unirme a una startup o empresa que se encuentre en aceleración, certificarme como Google Web Developer, y seguir una certificación de GCP o AWS. Practicar algoritmos difíciles."
    })