from tkinter import *
import webbrowser as wb

root=Tk()
root.title('webbrowser')
root.geometry('500x500')
l=Label(root,text='Webbrowser ',fg='red',bg='white',font=('arial black',15,'italic'),justify=CENTER)
l.pack()

l1=Label(root,text='search the website?',font=('arial black',15,'italic','bold'))
l1.place(x=50,y=100)

browser_link=StringVar()

def search():
    link=browser_link.get()
    wb.open_new(link)

e=Entry(root,textvariable=browser_link,font=('arial black',15,'italic','bold'))
e.place(x=350,y=100)

b=Button(root,text='search',command=search,width=12,height=4)
b.place(x=250,y=300)
root.mainloop()
