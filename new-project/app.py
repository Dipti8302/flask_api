# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import sqlite3

from flask import Flask, request
from pydantic import BaseModel
from flask_pydantic import validate
from typing import Optional

# from flask_pydantic import validator

class request_model(BaseModel):
    fname: str
    lname: str
    roll_no: int
    phone: Optional[int]

class response(BaseModel):
    fname: str
    lname: str
    roll_no: int
    phone: Optional[int]


app = Flask(__name__)
# @app.route("/")
# def index():
# return "string is working"


@app.route("/submit", methods=["POST"])
def save_details():
    """used to store details in database"""
    if request.method == "POST":
        data = request.get_json()
        fname = data['fname']
        lname = data['lname']
        roll_no = data['roll_no']
        phone = data['phone']
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""INSERT INTO student1(fname,lname,roll_no,phone)
        values(?,?,?,?)""", (fname, lname, roll_no, phone))
        con.commit()
        return {"Response":"Successful"}


@app.route("/getdata", methods=["GET"])
def get_details():
    """used to get details from database"""
    if request.method == "GET":
        # data=request.get_json()
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        # cur.execute("""CREATE TABLE student(fname varchar)""")
        cur.execute("""SELECT * FROM student1""")
        a_data = cur.fetchall()
        con.commit()
        return {"DATA":a_data}
"""Method to validate input data"""
@app.route("/post_data", methods=["POST"])
@validate()
def post_data(form:request_model):
    fname=form.fname
    lname=form.lname
    roll_no=form.roll_no
    phone=form.phone
    #return response(fname=fname,lname=lname,roll_no=roll_no,phone=phone)
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO student1(fname,lname,roll_no,phone)
        values(?,?,?,?)""", (fname, lname, roll_no, phone))
    con.commit()
    return {"Response":"Successful"}


@app.route("/student")
def get_student():
   con = sqlite3.connect("student.db")
   cur = con.cursor()
   cur.execute("""SELECT * FROM student1""")
   a_data = cur.fetchall()
   con.commit()
   return {"DATA:": a_data}

if __name__ == "__main__":
    app.run(debug=True)

