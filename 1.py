# import tkinter as  tk
# from tkinter import ttk
# from tkinter import scrolledtext
# root=tk.Tk()
# root.title("combobox")
# root.geometry("600x600")
# ttk.Label(root,text="python life",background="blue",foreground="white",
#         font=("times new roman",15)).grid(row=0,column=1)

# ComboBox
# n=tk.StringVar()
# course=ttk.Combobox(root,width=27,textvariable=n)
# course['values']=("python",
#                     "django",
#                     "machine learning")
# course.grid(column=1,row=5)
# course.current()

# root.mainloop()


# import tkinter as  tk
# from tkinter import ttk
# from tkinter import scrolledtext
# root=tk.Tk()
# root.title("scrolltext")
# root.geometry("600x600")
# ttk.Label(root,text="python life",background="blue",foreground="white",
#         font=("times new roman",15)).grid(row=0,column=1)
# #scrolltext
# text1=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=10)
# text1.grid(column=0,pady=10,padx=10)
# text1.focus()
# root.mainloop()



from subprocess import _TXT
from tkinter import*
root=Tk()
def send():
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>hi")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"bot=>hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"bot=>fine and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"bot=>okay")
    elif(e.get()=="what are you doing"):
        txt.insert(END,"\n"+"bot=>i am studing")
    elif(e.get()=="how is your studies"):
        txt.insert(END,"\n"+"bot=>good and you")
    elif(e.get()=="my studies also good"):
        txt.insert(END,"\n"+"bot=>okey bye")
    else:
        txt.insert(END,"\n"+"bot=>nice to hear")
    e.delete(0,END)
txt=Text(root,height=25,width=65)
txt.grid(row=0,column=0)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)

root.title("CHATBOX")
root.configure(bg="purple")


root.mainloop()
 