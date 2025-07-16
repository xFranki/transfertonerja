import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración SMTP desde variables de entorno
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Gmail user
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = (os.environ.get('MAIL_DEFAULT_SENDER_NAME', 'TransferToNerja'),
                                     os.environ.get('MAIL_USERNAME'))

mail = Mail(app)

# Ruta para guardar reservas (configurable por variable)
RESERVAS_FILE = os.environ.get('RESERVAS_FILE', 'reservas.txt')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservar', methods=['GET'])
def mostrar_reserva():
    return render_template('reservar.html')

@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    email_cliente = request.form['email']
    origen = request.form['origen']
    destino = request.form['destino']
    fecha = request.form['fecha']
    vuelo = request.form.get('vuelo')
    comentarios = request.form.get('comentarios', '')

    # Guardar en archivo (modo append)
    with open(RESERVAS_FILE, "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    # Email interno
    msg = Message("Nueva reserva Taxi", recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = f"""
Nueva reserva recibida:

Nombre: {nombre}
Teléfono: {telefono}
Email: {email_cliente}
Origen: {origen}
Destino: {destino}
Fecha y hora: {fecha}
Vuelo: {vuelo}
Comentarios: {comentarios}
"""
    mail.send(msg)

    # Email confirmación cliente
    msg_cliente = Message("Confirmación de tu reserva Taxi", recipients=[email_cliente])
    msg_cliente.body = f"""Hola {nombre},

Gracias por reservar con TransferToNerja.
Confirmamos tu reserva para el día {fecha} desde {origen} hacia {destino}.

Comentarios: {comentarios}

---
Hello {nombre},

Thank you for booking with TransferToNerja.
We confirm your booking for {fecha} from {origen} to {destino}.

Comments: {comentarios}

Un saludo / Best regards,
TransferToNerja
"""
    mail.send(msg_cliente)

    return render_template("confirmacion.html", nombre=nombre, origen=origen, destino=destino, fecha=fecha, vuelo=vuelo, comentarios=comentarios)


@app.route("/destinos")
def destinos():
    return render_template("destinos.html")

@app.route("/tarifas")
def tarifas():
    return render_template("tarifas.html")

# Inglés
@app.route('/en/')
def index_en():
    return render_template('en/index.html')

@app.route('/en/reservar', methods=['GET'])
def mostrar_reserva_en():
    return render_template('en/reservar.html')

@app.route('/en/reservar', methods=['POST'])
def reservar_en():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    email_cliente = request.form['email']
    origen = request.form['origen']
    destino = request.form['destino']
    fecha = request.form['fecha']
    vuelo = request.form.get('vuelo')
    comentarios = request.form.get('comentarios', '')

    with open(RESERVAS_FILE, "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    msg = Message("New Taxi Booking", recipients=[os.environ.get('MAIL_USERNAME')])
    msg.body = f"""
New booking received:

Name: {nombre}
Phone: {telefono}
Email: {email_cliente}
Origin: {origen}
Destination: {destino}
Date and time: {fecha}
Flight: {vuelo}
Comments: {comentarios}
"""
    mail.send(msg)

    msg_cliente = Message("Your Taxi Booking Confirmation", recipients=[email_cliente])
    msg_cliente.body = f"Hello {nombre},\n\nThank you for booking with us. We confirm your booking for {fecha} from {origen} to {destino}.\n\nComments: {comentarios}\n\nBest regards."
    mail.send(msg_cliente)

    return render_template("en/confirmacion.html", nombre=nombre, origen=origen, destino=destino, fecha=fecha, vuelo=vuelo, comentarios=comentarios)

from flask import request
@app.context_processor
def inject_current_path():
    return dict(current_path=request.path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)