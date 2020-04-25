from flask import Flask, redirect, render_template, request
import sqlite3 as lite

app= Flask(__name__)
connection = lite.connect('lecture.db', check_same_thread=False)
db = connection.cursor()

@app.route("/")
def index():
	db.execute("CREATE TABLE IF NOT EXISTS 'registrants' ('name' TEXT, 'phone' TEXT)")
	db.execute("SELECT * FROM registrants")
	rows = db.fetchall()
	return render_template("index.html", rows=rows)

@app.route("/register", methods=['GET','POST'])
def register():
	if request.method == "GET":
		return render_template("register.html")
	else:
		name = request.form.get('name')
		if not name:
			return render_template("apology.html", message="You must provide a name.")
		phone = request.form.get('phone')
		if not phone:
			return render_template("apology.html", message="You must provide a phone number.")
		db.execute('INSERT INTO registrants (name, phone) VALUES (?,?)', (name,phone))
		connection.commit()
		return redirect('/')
