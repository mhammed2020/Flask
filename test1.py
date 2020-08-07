from flask import Flask, render_template

app1 = Flask(__name__)


@app1.route("/")
def product_list():
    return render_template("index.html", title="Home | ",attr2 = " paragraph from index html")

@app1.route("/blog")
def product_detail():
    return render_template("detail.html", title=" More detail | ", attr2 = " paragraph from detail html")

@app1.route("/new")
def add_blog():
    return render_template("add.html", title=" new blog | ")


if __name__ == "__main__":
    app1.run(debug=True, port=9999)
