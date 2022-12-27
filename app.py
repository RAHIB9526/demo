
from flask import Flask, render_template, request, redirect

import pymysql

app = Flask(__name__)
# conn = pymysql.connect(host=data.host, port=data.port,
#                        user=data.user, passwd=data.password, db=data.db)
# db = yaml.safe_load(open('db.yaml'))
# conn = pymysql.connect(host=db['host'], port=db['port'],
#                        user=db['user'], passwd=db['password'], db=db['db'])
conn = pymysql.connect(host="demo-vpv-db.cwwagolhpeyz.ap-south-1.rds.amazonaws.com",
                       port=3306, user="admin", passwd="1234567890", db="test")


@ app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        age = userDetails['age']
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Info(NAME, AGE) VALUES( %s, %s)", (name, age))
        conn.commit()
        return redirect('/user')
    return render_template('index.html')


@ app.route('/user')
def user():
    cur = conn.cursor()
    result = cur.execute("SELECT *  FROM Info")
    if result > 0:
        userDetails = cur.fetchall()
        for detail in userDetails:
            var = detail
        return render_template('user.html', var=var)


if __name__ == '__main__':
    app.run()
