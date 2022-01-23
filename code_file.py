import tkinter as tk
from fpdf import FPDF
import pymysql
def atm_login():
    root=tk.Tk()
    root.title("Please enter details")
    root.geometry("1600x1200")
   
    title=tk.Label(root,text="Login",font=15)
    title.place(x=530,y=150)

    ul1=tk.Label(root,text="account no :",font=20)
    ul1.place(x=350,y=200)
    global u1
    u1=tk.Entry(root)
    u1.place(x=550,y=205)
   
    ul2=tk.Label(root,text="Pin :",font=20)
    ul2.place(x=350,y=250)
    global u2
    u2=tk.Entry(root)
    u2.place(x=550,y=255)
   
    b=tk.Button(root,text="Enter",font=20,command=login_valid)
    b.place(x=500,y=300)
   
    root.mainloop()
def login_2():
    root1=tk.Tk()
    root1.geometry("1600x1200")
   
    b4=tk.Button(root1,text="check balance",font=20,command=show)
    b4.place(x=550,y=100)
   
    b1=tk.Button(root1,text="cash withdrawal",font=20,command=wdr)
    b1.place(x=550,y=200)
   
    b2=tk.Button(root1,text="change pin",font=20,command=change)
    b2.place(x=550,y=300)
   
    b3=tk.Button(root1,text="mini statment",font=20,command=mini)
    b3.place(x=550,y=400)
    root1.mainloop()
   
def login_valid():
    global account1
    account=u1.get()
    account1=account
    global pwd
    pwd=u2.get()
    print(account,pwd)
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()
    query1="select pin from user_acc where account_no='"+account+"'and pin='"+pwd+"'"
    s.execute(query1)
    conn.commit()  
    row=s.fetchone()
    if(row):
        pinxy=int(row[0])
        pinxy=str(pinxy)
        print(type(pinxy))
        if(pwd == pinxy):
            login_2()              
    else:
        atm_login()
def show():
    root2=tk.Tk()
    root2.geometry("1600x1200")
    
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()  
    query2="select  amount from user_acc where account_no='"+account1+"'and pin='"+pwd+"'"
    s.execute(query2)
    conn.commit()
    row=s.fetchone()
    bal=int(row[0])
    print(bal)
    title=tk.Label(root2,text="Available Balance",font=20)
    title.place(x=350,y=300)
    title=tk.Label(root2,text=bal,font=10)
    title.place(x=650,y=300)
    root2.mainloop()
def wdr():
    root4=tk.Tk()
    root4.geometry("1600x1200")
   
    amt1=tk.Label(root4,text="enter amount :",font=20)
    amt1.place(x=350,y=200)
    global am1
    am1=tk.Entry(root4)
    am1.place(x=600,y=205)
    bu=tk.Button(root4,text="Enter",font=20,command=login_1)
    bu.place(x=550,y=300)    
    print(account1)
    root4.mainloop()

def sucess_trn():
    root7=tk.Tk()
    root7.title("Transection")
    root7.geometry("1600x1200")
    
    global am2
    am2=avamt-ae
    am2=str(am2)
    print(am2)
   
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()  
    query3="update user_acc set amount='"+am2+"'where account_no='"+account1+"'"
    s.execute(query3)
    conn.commit()
    amm2=float(am2)
    account=int(account1)  
    query9="insert into account_hist(account_no,amount) values('%d','%f')" %(account,amm2)
    s.execute(query9)
    conn.commit()
   
    title=tk.Label(root7,text="Transection Sucessful",font=20)
    title.place(x=400,y=350)
    root7.mainloop()
   
def inssf_bal():
    root11=tk.Tk()
    root11.title("Transection")
    root11.geometry("1600x1200")

    title=tk.Label(root11,text="Insufficient Balance",font=20)
    title.place(x=400,y=350)
    root11.mainloop()
   
def login_1():
    global ae
    ae=int(am1.get())
   
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()
    query2="select  amount from user_acc where account_no='"+account1+"'and pin='"+pwd+"'"
    s.execute(query2)
    conn.commit()
    row=s.fetchone()
    global avamt
    avamt=int(row[0])
    print(avamt)
   
    if(ae>avamt):
        inssf_bal()
    else:    
        sucess_trn()
        print(ae)
def change():
    root3=tk.Tk()
    root3.title("Change pin")
    root3.geometry("1600x1200")
   
    title=tk.Label(root3,text="Change Pin",font=20)
    title.place(x=450,y=200)
    ch=tk.Label(root3,text="Enter your Pin :",font=20)
    ch.place(x=300,y=300)
    global c
    c=tk.Entry(root3)
    c.place(x=600,y=305)
       
    bu1=tk.Button(root3,text="Enter",font=20,command=change_1)
    bu1.place(x=450,y=400)  
   
    root3.mainloop()
def change_2():
    root5=tk.Tk()
    root5.title("Change pin")
    root5.geometry("1600x1200")
   
    title=tk.Label(root5,text="Change Pin",font=20)
    title.place(x=450,y=200)
    np=tk.Label(root5,text="Enter new Pin :",font=20)
    np.place(x=300,y=300)
    global n
    n=tk.Entry(root5)
    n.place(x=550,y=305)
   
    np2=tk.Label(root5,text="Re-Enter new Pin :",font=20)
    np2.place(x=300,y=400)
    global n2
    n2=tk.Entry(root5)
    n2.place(x=550,y=405)
       
    np1=tk.Button(root5,text="Enter",font=20,command=change_3)
    np1.place(x=450,y=500)  
   
    root5.mainloop()
def sucess_pin():
    root6=tk.Tk()
    root6.title("Change pin")
    root6.geometry("1600x1200")
    
    title=tk.Label(root6,text="Your Pin is changed sucessfully",font=20)
    title.place(x=300,y=350)
    root6.mainloop()
def change_3():
    global np3
    np3=n.get()
    print(np3)
   
    global np4
    np4=n2.get()
    print(np4)
    if(np3==np4):
        conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
        s=conn.cursor()
        query5="update user_acc set pin='"+np3+"'where account_no='"+account1+"'"
        s.execute(query5)
        conn.commit()
        sucess_pin()
    else:
        change_2()
def change_1():
    global ch2
    ch2=c.get()
    print(type(ch2))
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()
    query4="select pin from user_acc where account_no='"+account1+"'and pin='"+pwd+"'"
    s.execute(query4)
    conn.commit()
    row=s.fetchone()
    pinx=int(row[0])
    pinx=str(pinx)
    print(type(pinx))
    if(pinx == ch2):
        change_2()
def mini():
    root10=tk.Tk()
    root10.title("Change pin")
    root10.geometry("1600x1200")
   
    title=tk.Label(root10,text="Mini statement :",font=20)
    title.place(x=400,y=100)
    conn=pymysql.connect(host='localhost',db='vivek_atm',user='root',password='root')
    s=conn.cursor()  
    query11="select  amount from account_hist where account_no='"+account1+"'"
    s.execute(query11)
    conn.commit()
    row=s.fetchall()
    print(row)
    lk=100
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=30)
    for i in range(0,len(row)):
        lk+=50
        mn=row[i]
        mn=float(mn[0])
        print(mn)
        m=tk.Label(root10,text=mn,font=15)
        m.place(x=400,y=lk)
        name=str(mn)
        pdf.cell(200,30,txt=name,ln=1,align="c")
    pdf.output("mini.pdf")
    root10.mainloop()
atm_login()
