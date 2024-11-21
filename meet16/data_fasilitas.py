from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "SEKOLAH"
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods=["POST", "GET"])
def simpan():
    kolam_renang = request.form["kolam_renang"]
    lift = request.form["lift"]
    kamera = request.form["kamera"]
    tahun = request.form["tahun"]
    
    cursor = mysql.connection.cursor()
    query = "INSERT INTO fasilitas (kolam_renang, lift, kamera, tahun) VALUES (%s, %s, %s, %s)"
    data = (kolam_renang, lift, kamera, tahun)
    cursor.execute(query, data)
    mysql.connection.commit()
    cursor.close()
    
    return "Data fasilitas berhasil disimpan."

@app.route('/tampil')
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM fasilitas")
    data = cursor.fetchall()
    cursor.close()
    
    return render_template("tampil.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
