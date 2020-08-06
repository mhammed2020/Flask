from flask import  Flask,render_template
app1 = Flask(__name__)

@app1.route("/")

def product_list():

    return render_template("index.html",title = "Home | ")
@app1.route("/blog")
def product_detail():
    return render_template("detail.html", dtitle = " More detail | ")

if __name__ =="__main__" :
    app1.run(debug=True,port=9999)