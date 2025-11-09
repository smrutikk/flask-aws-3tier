from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = pymysql.connect(
        host='flaskdb.cluster-c920ceeemm81.us-east-1.rds.amazonaws.com',  # Later this will be your RDS endpoint
        user='admin',
        password='123#Pass#',
        database='flaskdb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
