from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "GET":
    return render_template("index.html")
  if request.method == 'POST':
    emoji = request.form['emoji']
    # return render_template("output.html", emoji=emoji)
    return render_template("index.html", emoji=emoji)

app.run(host = "0.0.0.0", port = 8080)