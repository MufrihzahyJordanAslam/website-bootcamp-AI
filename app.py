
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template("index.html")

@app.route("/materi1")
def materi1():
    return render_template("materi1.html")

@app.route("/materi2")
def materi2():
    return render_template("materi2.html")

@app.route("/materi3")
def materi3():
    return render_template("materi3.html")

@app.route("/materi4")
def materi4():
    return render_template("materi4.html")

@app.route("/materi5")
def materi5():
    return render_template("materi5.html")

@app.route("/materi6")
def materi6():
    return render_template("materi6.html")

@app.route("/materi7")
def materi7():
    return render_template("materi7.html")

@app.route("/materi8")
def materi8():
    return render_template("materi8.html")

@app.route("/materi9")
def materi9():
    return render_template("materi9.html")

@app.route("/materi10")
def materi10():
    return render_template("materi10.html")

@app.route("/sertifikat")
def sertifikat():
    return render_template("sertifikat.html")


if __name__ == "__main__":
    app.run(debug=False)
