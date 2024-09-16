from flask import Flask, render_template, url_for, redirect, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def qwert():
    return render_template('about.html')


@app.route('/qwert')
def her():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='medi'
        )
        cursor = db.cursor()
        query = "INSERT INTO pat (username,password) VALUES (%s,%s)"
        cursor.execute(query, (username, password))
        db.commit()
        cursor.close()
        db.close()
        message = ''
        if request.method == 'POST':
            message = 'Login successful'
        return render_template('login.html', message=message)
    except mysql.connector.Error as err:
        return f'error: {err}'


@app.route('/role')
def role():
    return render_template('role.html')


@app.route('/patsign')
def patsign():
    return render_template('patsign.html')


@app.route('/docsign')
def docsign():
    return render_template('docsign.html')


if __name__ == '__main__':
    app.run(debug=True)
