import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

def connect_db():
    conn=sqlite3.connect("mydb.db")
    return conn

def create_table():
    conn=connect_db()
    cur=conn.cursor()
    cur.execute('create table if not exists student(name text,password text,roll_no int primary key,branch text)')
    conn.commit()
    conn.close()

def addrecord(data):
    
    conn=connect_db()
    cur=conn.cursor()
    try:
        cur.execute('insert into student(name,password,roll_no,branch)values(?,?,?,?)',data)
        conn.commit()
        st.success("you did it")
        conn.close()
    except sqlite3.IntegrityError:
        st.error("user already exist")
        
        conn.close()
    
  
    
def view_record():
    conn=connect_db()
    cur=conn.cursor()
    cur.execute('select * from student')
    result=cur.fetchall()
    conn.close()
    return result
def disp():
    data=view_record()
    st.table(data)
    
def sign_up():
    st.title("sign up")
    roll_no=st.text_input('enter your roll_no.')
    name=st.text_input('enter your name')
    branch=st.selectbox("branch",options=['cse','aiml','ece','me'])
    password=st.text_input('password',type='password')
    re_pass=st.text_input('re-try',type='password')
    if st.button("signin"):
        if password != re_pass:
            st.error("pass not matched")
        else:
            addrecord((name,password,roll_no,branch))
create_table()
with st.sidebar:
    select=option_menu('select from here',['sign_up','display all record'])
    
if select =='sign_up':
    sign_up()
else:
    disp()
    
