from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'bxberpbckwprklutgreb-mysql.services.clever-cloud.com'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'u4mubqleu8yekfle'
app.config['MYSQL_PASSWORD'] = '7IDR0tBd0CRwa78ATVSa'
app.config['MYSQL_DB'] = 'bxberpbckwprklutgreb'
app.config['MYSQL_URI'] = 'mysql://u4mubqleu8yekfle:7IDR0tBd0CRwa78ATVSa@bxberpbckwprklutgreb-mysql.services.clever-cloud.com:3306/bxberpbckwprklutgreb'
mysql = MySQL(app)

@app.route('/api/employee')
@cross_origin()
def getAllEmployees():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, address FROM employees')
    data = cur.fetchall()
    result = []
    for row in data:
        content = {
                'id':row[0],
                'firstname': row[1],
                'lastname': row[2],
                'email': row[3],
                'address': row[4]
            }
        result.append(content)
    return jsonify(result)

@app.route('/api/employee/<int:id>')
@cross_origin()
def getEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, address FROM employees WHERE id = ' + str(id))
    data = cur.fetchall()
    content = {}
    for row in data:
        content = {
                'id':row[0],
                'firstname': row[1],
                'lastname': row[2],
                'email': row[3],
                'address': row[4]
            }
    return jsonify(content)

@app.route('/api/employees', methods=['POST'])
@cross_origin()
def createEmployee():
    if 'id' in request.json:
        updateEmployee()
    else:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `employees` (`id`, `firstname`, `lastname`, `email`, `address`) VALUES (NULL, %s, %s, %s, %s);",
                    (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['address']))
        mysql.connection.commit()
        return "Cliente guardado"

def updateEmployee():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE `employees` SET `firstname` = %s, `lastname` = %s, `email` = %s, `address` = %s WHERE `employees`.`id` = %s;",
                (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['address'], request.json['id']))
    mysql.connection.commit()
    return "Cliente guardado"

@app.route('/api/employee/<int:id>', methods=['DELETE'])
@cross_origin()
def removeEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `employees` WHERE `employees`.`id` = " + str(id))
    mysql.connection.commit()
    return "Cliente eliminado"

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/<path:path>')
@cross_origin()
def publicFiles(path):
    return render_template(path)

if __name__ == '__main__':
    app.run(None, 3000, True)