from flask import Flask, request, redirect
from html import escape

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form = """
    <form action="/signup" method="post">
        <label>
            Username      
            <input type="text" name="user-name" value='{username}'/>
        </label>
        <br>
        <label>
            Password
            <input type="password" name="pass-word" value='{password}'/>
        </label>
        <br>
        <label>
            Verify Password
            <input type="password" name="ver-pass-word" value='{ver_password}'/>
        </label>
        <br>
        <label>
            Email (optional)
            <input type="text" name="e-mail" value='{email}'/>
        </label>
        <br>
        <input type="submit" value="Submit"/>
    </form>
"""

@app.route("/signup", methods=['POST'])
def index():
    username = request.form['user-name']
    password = request.form['pass-word']
    ver_password = request.form['ver-pass-word']
    email = request.form['e-mail']
    error = ''
    #make sure user-name is valid
    if username == '':
        pass
    #make sure pass-word is valid
    if password == '':
        pass
    #make sure ver-password matches
    if ver_password != password:
        pass
    #make sure email is valid
    if email == '':
        pass

    content = form
    return content

@app.route("/")
def submit_form():
    content = form
    return content.format(username='', password='', ver_password='', email='')

app.run()
