from flask import Flask, render_template

#Inicialización de flask
#__name__ variable de python indica que es el archivo principal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

@app.route('/about')
def about():
    return render_template('about.html')


#validación para comprobar si se está en el archivo principal o un modulo
if __name__ == '__main__':
    app.run(debug=True)

