import sqlite3, os, hashlib
from flask import *

app = Flask(__name__)
app.database = "sample.db"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods = ["POST", "GET"])
def success():
		if request.method == "POST":
			result = request.form.get('name')
			return '''<p> Hello </p> <p>''' + result + '''</p>
			<a href = menu ><button>MENU</button></a> '''

@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/search', methods = ['POST'])
def search():
	connection = connect_db()
	cur = connection.cursor()
	if request.method == "POST":
		item = request.form.get('item')
		result = cur.execute("SELECT * FROM items where name = '%s'" %item)
		details = cur.fetchall()
		return render_template('search.html', details = details)
	

def connect_db():
	return sqlite3.connect(app.database)

if __name__ == '__main__':

	if not os.path.exists(app.database):
		with sqlite3.connect(app.database) as connection:
			c = connection.cursor()
			c.execute('CREATE TABLE items(name TEXT, price TEXT)')
			c.execute('CREATE TABLE employees(username TEXT, password TEXT)')
			c.execute('INSERT INTO items VALUES("rice", "110")')
			c.execute('INSERT INTO items VALUES("flour", "100")')
			c.execute('INSERT INTO employees VALUES("ravi", "abc")')
			c.execute('INSERT INTO employees VALUES("mark", "def")')
			c.execute('INSERT INTO employees VALUES("jason", "ghi")')
			connection.commit()
			
	app.run(debug = True)