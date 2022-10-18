
from flask import *

import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "vishal"
    )

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")     # Heading in website 1st page

@app.route("/contact")
def contact():
    return render_template("contact1.html")

@app.route("/about")
def about():
    name = "VISHAL SONTAKKE"
    mylist = [95,52,29,35,54]
    return render_template("about1.html",name = name,mylist = mylist)

@app.route("/allusers")
def allusers():
    cursor.execute("select * from students")
    data = cursor.fetchall()
    return render_template("allusers1.html",userdata = data)

@app.route("/user/<name>")
def user(name):
    return "Hello {}".format(name)


@app.route("/create",methods=["POST"])
def create():
    
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    contact = request.form.get('contact')
    
    
    insq = "insert into students(Name,Age,Belt) values ('{}','{}','{}')".format(uname,pwd,contact)
    
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"
@app.route("/delete")
def delete():
    id=request.args.get('id')
    
    
    delq= "delete from students where id={}".format(id)
    
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"

@app.route("/edit")
def edit():
    id=request.args.get('id')
    
    seql = "select * from students where id={}".format(id)
    cursor.execute(seql)
    data=cursor.fetchone()
    return render_template("edit1.html",row=data)

@app.route("/edit",methods=["POST"])
def update():
    
    
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    contact = request.form.get('contact')
    uid = request.form.get("uid")    
    upd = "update students set name='{}',age='{}',belt='{}' where id='{}'".format(uname,pwd,contact,uid)
        
    try:
        cursor.execute(upd)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in query"

@app.route("/search")
def search():
    return render_template("search1.html")


@app.route("/getdata",methods=["POST"])
def getdata():
    id=request.form.get('id')
    seql= "select * from students where id = {}".format(id)
    
    cursor.execute(seql)
    data = cursor.fetchone()
    return render_template("search1.html",row=data)



if __name__ == '__main__':
    app.run()
    
    
