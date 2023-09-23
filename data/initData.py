import sqlite3
import os

os.system(f'rm data.db')
os.system(f'type nul > data.db')
name = './data.db'

con = sqlite3.connect(name)
cur = con.cursor()

cur.execute("""
    create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
""")

cur.execute("""
    create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
""")

print('done!')