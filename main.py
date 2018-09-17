from flask import Flask, request, redirect, render_template, escape
import os
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

class Error:
    def __init__(self):
        self.username_error=''
        self.password_error=''
        self.ver_password_error=''
        self.email_error=''

    def is_error(self):
        if (self.username_error or 
            self.password_error or 
            self.ver_password_error or
            self.email_error):
            return True
        else:
            return False
    
    def __bool__(self):
        return self.is_error()

    def clear(self):
        self.__init__()

error = Error()

@app.route("/signup", methods=['POST'])
def index():
    username = request.form['user-name']
    password = request.form['pass-word']
    ver_password = request.form['ver-pass-word']
    email = request.form['e-mail']
    #it contains a space character or it consists of less than 3 characters or more than 20 characters
    #make sure user-name is valid
    error.clear()
    if username == '':
        error.username_error += 'Please enter a username. '
    if 20 < len(username) or len(username) < 3:
        error.username_error += 'Username must be 3 to 20 characters long. '
    if username.find(' ')!=-1:
        error.username_error += 'Username cannot contain spaces. '
    #make sure pass-word is valid
    #it contains a space character or it consists of less than 3 characters or more than 20 characters
    if 20 < len(password):
        error.password_error += 'Password must be under 21 characters long. '
    elif len(password) < 3 :
        error.password_error += 'Password must be over 2 characters long. '
    if password.find(' ')!=-1:
        error.password_error += 'Password cannot contain spaces. '
    #make sure ver-password matches
    if ver_password != password:
        error.ver_password_error += 'Passwords did not match. '
    #make sure email is valid
    # contains a single @, a single ., contains no spaces, and is between 3 and 20 characters long
    if email != '':
        if not re.match(r'^\S+@\S+\.\S+', email):
            error.email_error += 'Email must contain a single @, a single period, no spaces'
        if len(email)<3:
            error.email_error += 'Must be longer than 2 characters. '
        if len(email)>20:
            error.email_error += 'Must be shorter than 20 characters. '
        #and 3-20 characters long. '
        #if email.count('@')!=1 or email.count('.')!=1 or email.find(' ')!=-1 or 20 < len(email) < 3:

    if error:
        return render_template('input_form.html',title='Signup Form',username=username, email=email, error=error)
    else:
        return redirect("/welcome?username="+ username)

@app.route("/")
def submit_form():
    return render_template('input_form.html',title='Signup Form', input='Signup Form',error=error)

@app.route("/welcome")
def welcome_form():
    print('welcome page')
    username = request.args.get("username")
    return render_template('welcome.html', title='Welcome Page', username=username)

app.run()
