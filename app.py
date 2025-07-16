'''from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor SMTP (ejemplo con Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'frannerja1@gmail.com'
app.config['MAIL_PASSWORD'] = 'xkic dsyd fdrr wmqo'
app.config['MAIL_DEFAULT_SENDER'] = ('Reserva VTC', 'tucorreo@gmail.com')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

# Mostrar el formulario de reserva
@app.route('/reservar', methods=['GET'])
def mostrar_reserva():
    return render_template('reservar.html')

# Procesar los datos del formulario
@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    email_cliente = request.form['email']
    origen = request.form['origen']
    destino = request.form['destino']
    fecha = request.form['fecha']
    vuelo = request.form.get("vuelo")
    comentarios = request.form.get('comentarios', '')

    # Guardar reserva en archivo
    with open("reservas.txt", "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    # Email para ti
    msg = Message("Nueva reserva VTC",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['frannerja1@gmail.com'])
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

    # Email de confirmación para el cliente
    msg_cliente = Message("Confirmación de tu reserva VTC",
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[email_cliente])
    msg_cliente.body = f"Hola {nombre},\n\nGracias por reservar con nosotros. Confirmamos tu reserva para el día {fecha} desde {origen} hacia {destino}.\n\nComentarios: {comentarios}\n\nSaludos."
    mail.send(msg_cliente)

    return render_template("confirmacion.html", nombre=nombre, origen=origen, destino=destino, fecha=fecha, vuelo=vuelo, comentarios=comentarios)

@app.route("/destinos")
def destinos():
    return render_template("destinos.html")

@app.route("/tarifas")
def tarifas():
    return render_template("tarifas.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/en')
def home_en():
    return render_template('en/index.html')
'''

'''from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del servidor SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'frannerja1@gmail.com'
app.config['MAIL_PASSWORD'] = 'xkic dsyd fdrr wmqo'
app.config['MAIL_DEFAULT_SENDER'] = ('Reserva Taxi', 'tucorreo@gmail.com')

mail = Mail(app)

# --- RUTAS EN ESPAÑOL ---

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
    vuelo = request.form.get("vuelo")
    comentarios = request.form.get('comentarios', '')

    with open("reservas.txt", "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    msg = Message("Nueva reserva Taxi", sender=app.config['MAIL_USERNAME'], recipients=['frannerja1@gmail.com'])
    msg.body = f"""Nueva reserva recibida:

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

    msg_cliente = Message("Confirmación de tu reserva Taxi", sender=app.config['MAIL_USERNAME'], recipients=[email_cliente])
    msg_cliente.body = f"Hola {nombre},\n\nGracias por reservar con nosotros. Confirmamos tu reserva para el día {fecha} desde {origen} hacia {destino}.\n\nComentarios: {comentarios}\n\nSaludos."
    mail.send(msg_cliente)

    return render_template("confirmacion.html", nombre=nombre, origen=origen, destino=destino, fecha=fecha, vuelo=vuelo, comentarios=comentarios)

@app.route("/destinos")
def destinos():
    return render_template("destinos.html")

@app.route("/tarifas")
def tarifas():
    return render_template("tarifas.html")


# --- RUTAS EN INGLÉS ---

@app.route('/en')
def home_en():
    return render_template('en/index.html')

@app.route('/en/reservar', methods=['GET'])
def show_booking_en():
    return render_template('en/reservar.html')

@app.route('/en/reservar', methods=['POST'])
def book_en():
    # Aquí puedes duplicar la lógica de reserva en inglés si deseas personalizar mensajes
    return redirect(url_for('home_en'))


# --- MAIN ---

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/en/')
def index_en():
    return render_template('en/index.html')

@app.route('/en/tarifas')
def tarifas_en():
    return render_template('en/precios.html')

@app.route('/en/destinos')
def destinos_en():
    return render_template('en/destinos.html')

@app.route('/en/reservar')
def reservar_en():
    return render_template('en/book.html')'''


from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'transfertonerja@gmail.com'
app.config['MAIL_PASSWORD'] = 'uyrk rbep khxn ldui'  # O usa una contraseña de aplicación si tienes verificación en 2 pasos
app.config['MAIL_DEFAULT_SENDER'] = ('TransferToNerja', 'transfertonerja@gmail.com')


mail = Mail(app)

# --- RUTAS EN ESPAÑOL ---

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

    # Guardar reserva
    with open("reservas.txt", "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    # Email a ti
    msg = Message("Nueva reserva Taxi", sender=app.config['MAIL_USERNAME'], recipients=['transfertonerja@gmail.com'])
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
    msg_cliente = Message("Confirmación de tu reserva Taxi", sender=app.config['MAIL_USERNAME'], recipients=[email_cliente])
    
    msg_cliente.body = f"""Hola {nombre},

    Gracias por reservar con TransferToNerja.

    Confirmamos tu reserva para el día {fecha} desde {origen} hacia {destino}.

    Comentarios: {comentarios}

    Nos pondremos en contacto contigo si necesitamos más información.

    ---

    Hello {nombre},

    Thank you for booking with TransferToNerja.

    We confirm your booking for {fecha} from {origen} to {destino}.

    Comments: {comentarios}

    We’ll contact you if we need any more information.

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

# --- RUTAS EN INGLÉS ---

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

    with open("reservas.txt", "a") as f:
        f.write(f"{nombre}, {telefono}, {email_cliente}, {origen}, {destino}, {fecha}, {vuelo}, {comentarios}\n")

    msg = Message("New Taxi Booking", sender=app.config['MAIL_USERNAME'], recipients=['transfertonerja@gmail.com'])
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

    msg_cliente = Message("Your Taxi Booking Confirmation", sender=app.config['MAIL_USERNAME'], recipients=[email_cliente])
    msg_cliente.body = f"Hello {nombre},\n\nThank you for booking with us. We confirm your booking for {fecha} from {origen} to {destino}.\n\nComments: {comentarios}\n\nBest regards."
    mail.send(msg_cliente)

    return render_template("en/confirmacion.html", nombre=nombre, origen=origen, destino=destino, fecha=fecha, vuelo=vuelo, comentarios=comentarios)

@app.route('/en/destinos')
def destinos_en():
    return render_template('en/destinos.html')

@app.route('/en/tarifas')
def tarifas_en():
    return render_template('en/tarifas.html')

from flask import request

@app.context_processor
def inject_current_path():
    return dict(current_path=request.path)

if __name__ == "__main__":
    app.run(debug=True)
