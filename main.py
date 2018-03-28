from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

formU = """
<!DOCTYPE html>

<html>
    <head>
        <style> .error {{ color: red; }} </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" />
                        <span class="error">{pswrdfail}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    fill_in_content = formU
    return fill_in_content






@app.route("/", methods=['POST'])
def password_validate():  #Password verification
    passwordA = request.form['password']
    verifyA = request.form['verify']
    invalid_char = ''   #tests for " " in pw p1
    pwX = 0             #tests pw length p1
    for char in passwordA:
        pwX = pwX + 1
        if char == " ":   #tests for " " in pw p2
            invalid_char = "Invalid Character. Cannot contain 'space'"
    if invalid_char == "Invalid Character. Cannot contain 'space'":      
        return formU.format(pswrdfail=invalid_char)
    if passwordA == '':     #Test for blank pw
        pwsblank = "Password can not be blank, dumbass."
        return formU.format(pswrdfail=pwsblank)
    if pwX < 3 or pwx > 20:       #tests pw length p2
        pwlngth = "Password must be 3 - 20 characters."
        return formU.format(pswrdfail=pwlngth)           
    if passwordA != verifyA: #Tests to see if pws match
        nomatch = "Passwords do not match, idiot."
        return formU.format(pswrdfail=nomatch)



###This is dead currently
@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)



        


app.run()