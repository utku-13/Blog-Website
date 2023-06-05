from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/blog")
def blogp():
    p = Post()
    data = p.get_data()
    return render_template("post.html",dt=data,num=0)

@app.route("/blog1")
def blogp1():
    p = Post()
    data = p.get_data()
    return render_template("post.html",dt=data,num=1)

if __name__ == "__main__":
    app.run(debug=True)
