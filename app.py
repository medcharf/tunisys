from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Simulated user database (replace with your actual user authentication logic)
users = {'user': 'password'}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('loader', next_page='loggedin'))
        else:
            return render_template('login.html', message='Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/loggedin')
def loggedin():
    if 'username' in session:
        return render_template('loggedin.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/getcode')
def getcode():
    if 'username' in session:
        return render_template('getcode.html')
    else:
        return redirect(url_for('login'))

'''@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')'''

    

@app.route('/loader')
def loader():
    next_page = request.args.get('next_page')
    return render_template('loader.html', next_page=next_page)

if __name__ == '__main__':
    app.run(debug=True)
