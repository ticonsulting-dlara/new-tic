from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
from pathlib import Path

app = Flask(__name__, static_folder='assets')
app.secret_key = 'change-this-key'

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html', title='TI Consulting')

@app.route('/servicios/')
def servicios():
    return render_template('servicios.html', title='Servicios')

@app.route('/chat/')
def chat():
    return render_template('chat.html', title='Chat')

@app.route('/quienes-somos/')
def quienes_somos():
    return render_template('quienes_somos.html', title='Quiénes Somos')

@app.route('/partners/')
def partners():
    return render_template('partners.html', title='Partners')

@app.route('/nuestros-clientes/')
def nuestros_clientes():
    return render_template('nuestros_clientes.html', title='Nuestros Clientes')

@app.route('/contacto/', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        flash('Mensaje enviado correctamente')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', title='Contacto')

@app.route('/declaracion-de-privacidad/')
def declaracion_de_privacidad():
    return render_template('declaracion_de_privacidad.html', title='Declaración de Privacidad')

@app.route('/terminos-y-condiciones/')
def terminos_y_condiciones():
    return render_template('terminos_y_condiciones.html', title='Términos y Condiciones')

@app.route('/send_contact', methods=['POST'])
def send_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    data = {
        'name': name,
        'email': email,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }

    contacts_file = Path('contacts.json')
    if contacts_file.exists():
        existing = json.loads(contacts_file.read_text())
    else:
        existing = []
    existing.append(data)
    contacts_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False))

    flash('Gracias por contactarnos.')
    return redirect(url_for('contacto'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Página no encontrada'), 404

if __name__ == '__main__':
    app.run(debug=True)
