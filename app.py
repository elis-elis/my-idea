from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    pass


@app.route("/blog-area", methods=["GET"])
def blogs():
    return render_template("blog_area.html")
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
