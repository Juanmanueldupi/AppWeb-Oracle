from flask import Flask, request, render_template
import cx_Oracle

app = Flask(__name__)
# Configura la conexión a la base de datos Oracle
dsn = cx_Oracle.makedsn('localhost', 1521, 'ORCLCDB')
connection = cx_Oracle.connect('jmdp', 'jmdp', dsn)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/result', methods=['POST'])
def result():
    username = request.form['username']
    password = request.form['password']

    # Verifica las credenciales
    if username == 'jmdp' and password == 'jmdp':
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Partidos')
        data = cursor.fetchall()
        cursor.close()
        return render_template('result.html', data=data)
    else:
        return "Credenciales incorrectas"

if __name__ == '__main__':
    app.run()