from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/enviar_respuesta', methods=['POST'])
def enviar_respuesta():
    nombre = request.form['nombre']
    asistencia = request.form['asistencia']
    mensaje = request.form['mensaje']
    with open('respuestas.txt', 'a') as f:
        f.write(f"Nombre: {nombre}, Asistencia: {asistencia}, Mensaje: {mensaje}\n")
    return 'Respuesta enviada'

if __name__ == '__main__':
    app.run(debug=True)