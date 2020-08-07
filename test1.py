from flask import Flask, render_template

app1 = Flask(__name__)

prods =[("Tshirts",39),("Shoes",57),("PC",67)]
@app1.route("/")
def product_list():
    return render_template("index.html", title="Home | ",css_file = "index")

@app1.route("/blog")
def product_detail():
    return render_template("detail.html", title=" More detail | ")

@app1.route("/new")
def add_blog():
    return render_template("add.html", title=" new blog | ", css_file = "add")
@app1.route("/items")
def products():
    return render_template("products.html", title="Products",p_head = "products",
                           desc="this my products space ",
                           prods = prods,css_file = "products")


if __name__ == "__main__":
    app1.run(debug=True, port=9999)
