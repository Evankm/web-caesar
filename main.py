
from flask import Flask, request, render_template
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 2S0px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 150px;
            }
        </style>
    </head>
    <body>
    <div>
    <br><br><br><br><br><br>
    <form method="post">
    <input type="text" name="shift" placeholder="Enter Number...">
    <textarea rows="4" cols="50" name="plaintext" placeholder="Enter Message..."></textarea>
    <input type="submit" value="Submit">
    </form>
    </div>
      <!-- create your form here -->
    </body>
</html>
"""
    
@app.route("/")
def index():
    return form

@app.route('/', methods=['GET','POST'])
def encryption():
    if request.method == 'POST':
        shift = request.form['shift']
        plaintext = request.form['plaintext']
        shift = int(shift)
        new_message = encrypt(plaintext, shift)    
        return  render_template('index.html', new_message = new_message)
        
'''def encryption ():
    text1 =''
    shift = ''
    for field in request.form.keys():
        text1  += "<b>{value}</b> ".format(key=field,
        #shift += "<b> {value}</b>".fromat(key=field,
        value =  request.form[field])
    text2 = 0
    for val in text1:
        if type(val) == int:
            text2 = val

    return text1, text2 '''

app.run()