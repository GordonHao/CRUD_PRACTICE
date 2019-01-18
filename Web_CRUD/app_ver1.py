from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("select * FROM class")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', classes=rv)


@app.route('/Save', methods=["POST"])
def Save():
    classs = request.form['class']
    name = request.form['name']
    gender = request.form['gender']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO class (class, name, gender) VALUES (%s, %s, %s)",(classs, name, gender,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update():
    Num_data = request.form['Num']
    classs = request.form['class']
    name = request.form['name']
    gender = request.form['gender']
    cur = mysql.connection.cursor()
    cur.execute("update class SET class=%s, name=%s, gender=%s WHERE Num=%s",(classs, name, gender, Num_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:Num_data>', methods=["GET"])
def delete(Num_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM class WHERE Num=%s",(Num_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
