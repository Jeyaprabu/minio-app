# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:51:01 2016

@author: Jeyaprabu J
"""

from Tkinter import *
import tkMessageBox
from minio import Minio
main=cli=ent=None

def listbucket():
    global cli
    li=Tk()
    allbuc=""
    buckets = cli.list_buckets()
    for bucket in buckets:
        allbuc=allbuc+"\n"+"Bucket Name: "+bucket.name+"\n"
    lab=Label(li,text=allbuc)
    lab.pack()
    li.mainloop()
    

def makebucket():
    global cli,ent
    bucname=ent.get()
    try:
        cli.make_bucket(bucname)
        tkMessageBox.showinfo(title="Minio Server",message="bucket created successfully")
    except:
        tkMessageBox.showinfo(title="Minio Server",message="error in making bucket")

def mbw():
    try:
        global cli,ent
        main.withdraw()
        mb=Tk()
        lab1=Label(mb,text="Enter the new Bucket name")
        lab1.grid(row=0,column=0,sticky="E")
        ent=Entry(mb)
        ent.grid(row=0,column=1,sticky="W")
        but=Button(mb,text="create bucket",relief="groove",borderwidth="4",command=makebucket)
        but.grid(row=1,column=1,sticky="E")
        mb.mainloop()
    except:
        tkMessageBox.showinfo(title="Minio Server",message="error in makebucket window")

def operations():
    try:
        op=Tk()
        but1=Button(op,text="Make new bucket",relief="groove",borderwidth="4",command=mbw)
        but1.grid(row=0,column=0,sticky="E")
        but2=Button(op,text="List all buckets",command=listbucket)
        but2.grid(row=0,column=1,sticky="W")
        but3=Button(op,text="Remove bucket",command=makebucketwindow)
        but3.grid(row=1,column=0,sticky="E")
        but4=Button(op,text="List all buckets",command=listbucket)
        but4.grid(row=1,column=1,sticky="W")
        op.mainloop()
    except:
        tkMessageBox.showinfo(title="Minio Server",message="error in options window")

def auth():
    global main,cli
#    u=url.get()
#    s=secure.get()
#    a=access.get()
    u="172.16.23.1:9000"
    a="9P8O9WVH4PIB3XTAALX2"
    s="6cODbsYQbLgO1REd4DaNFecPf2kRYTggMRtCLsu2"
    try:
        cli=Minio(u,access_key=a,secret_key=s,insecure="true")
        tkMessageBox.showinfo(title="Minio Server",message="connected successfully")
        operations()
    except:
        tkMessageBox.showinfo(title="Minio Server",message="unable to connect to minio server...review connection parameters")
        
    
    
    

main=Tk()

note=Label(main,text="Connect with Minio Server")
note.grid(row=0,column=1,sticky="N")

ulabel=Label(main,text="URL")
ulabel.grid(row=1,column=0,sticky="E")

url=Entry(main)
url.grid(row=1,column=1,sticky="EW")

alabel=Label(main,text="Access key")
alabel.grid(row=2,column=0,sticky="E")

access=Entry(main)
access.grid(row=2,column=1,sticky="W")

slabel=Label(main,text="Secure key")
slabel.grid(row=3,column=0,sticky="E")

secure=Entry(main)
secure.grid(row=3,column=1,sticky="W")

button=Button(main,text="connect",relief="groove",borderwidth="4",command=auth)
button.grid(column=1,row=4,sticky="WS")

main.mainloop()