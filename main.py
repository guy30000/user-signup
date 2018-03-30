from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    #return formU
    #encoded_error = request.args.get("error")
    return render_template('editA.html')#, watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))



@app.route("/", methods=['POST'])
def password_validate():  #Actually all validate
    #Password Validation
    passwordA = request.form['password']
    verifyA = request.form['verify']
    usernameA = request.form['username']
    emailA = request.form['email']

    invalid_char = ''   #tests for " " in pw p1
    pwX = 0             #tests pw length p1
    uidX = 0            #tests uid length p1
    emlX = 0             #tests email length

    pswrdfailA = ''
    usernamefailA = ''
    emailfailA = ''
    at_test = ''
    dot_test = ''
    #pwd
    for char in passwordA:
        pwX = pwX + 1
        if char == " ":   #tests for " " in udi
            pswrdfailA = "Invalid Character. Cannot contain 'space'"
    if passwordA == '':     #Test for blank uid
         pswrdfailA = "Password can not be blank, dumbass."
    elif pwX < 3 or pwX > 20:       #tests pw length 
        pswrdfailA = "Password must be 3 - 20 characters."
    elif passwordA != verifyA: #Tests to see if pws match
        pswrdfailA = "Passwords do not match, idiot."
    #UID
    for char in usernameA:
        uidX =  uidX + 1
        if char == " ":   #tests for " " in UID
            usernamefailA = "User ID cannot contain 'space'"
    if uidX < 3 or uidX > 20:
        usernamefailA = "User ID must be 3 - 20 characters."
    if usernameA == '':     #Test for blank UID
         usernamefailA = "You must enter a user ID."
    #email
    for char in emailA:
        emlX = emlX + 1
        if char == " ":   #tests for " " in emial
            emailfailA = "Email addresses dont have spaces, jerk."
        if char == "@":    #tests for @ and .
            at_test = emlX
        if char == ".":
            dot_test = emlX
    if emlX < 3 or emlX > 20:   #tests length.
        emailfailA = "Email must be 3 - 20 characters, for some reason." 
    if at_test and dot_test:   #tests for @ and . in correct order
        if at_test < dot_test:
            testvaraible_unused = "pass"
        else:
            emailfailA = "Invalid email."
    else:
        emailfailA = "Invalid email." 

    if emlX == 0:    # ignores count if email is blank
            emailfailA = ''





    if pswrdfailA or usernamefailA or emailfailA:    
        return render_template('editA.html', usernamefailB=usernamefailA, pswrdfailB=pswrdfailA, emailfailB=emailfailA)
    else: 
        return render_template('hello_greeting.html', usernameB=usernameA)



app.run()