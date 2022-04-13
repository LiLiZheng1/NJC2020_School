from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/search',methods = ["POST"])
def search():
    data = request.form

    school_name = data["School"]
    department = data["Department"]

    connection = sqlite3.connect("schools.db")
    cursor = connection.execute("SELECT * FROM Schools,Staff WHERE Schools.SchoolName LIKE ? and Staff.Department = ?",("%" +school_name+"%",department)).fetchall()
    connection.commit()

    connection.close()

    return render_template("results_teacher_found.html",cursor = cursor )


if (__name__) == "__main__":
    app.run(debug = True, use_reloader = True)
