from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/username")

def index():
    flash("What is the device username")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def username():
    flash(str(request.form['name_input']))
    return render_template("index.html")
