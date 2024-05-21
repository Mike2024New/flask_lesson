from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html", text="first lesson")


@app.route("/about")
def about():
    return render_template("about.html", text="about")


if __name__ == '__main__':
    app.run(debug=True)
