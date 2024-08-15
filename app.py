from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog-area", methods=["GET"])
def blogs():
    return render_template("blog_area.html")


@app.route("/poem1")
def poem1():
    return render_template('poem1.html')


@app.route("/poem2")
def poem2():
    return render_template('poem2.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
