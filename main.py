from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    Entry_Dosa.delete(0,END)
    Entry_Idli.delete(0,END)
    Entry_Appe.delete(0,END)
    Entry_Noodles.delete(0,END)
    Entry_VeggieBurger.delete(0,END)
    Entry_PaneerBurger.delete(0,END)
    Entry_ColdDrinks.delete(0,END)
    
def Total():
    try:a1=int(Dosa.get())
    except: a1=0
    
    try:a2=int(Idli.get())
    except: a2=0
    
    try:a3=int(Appe.get())
    except: a3=0
    
    try:a4=int(Noodles.get())
    except: a4=0
    
    try:a5=int(VeggieBurger.get())
    except: a5=0
    
    try:a6=int(PaneerBurger.get())
    except: a6=0
    
    try:a7=int(ColdDrinks.get())
    except: a7=0
    
    #define cost of each item per quantity
    c1=60*a1
    c2=50*a2
    c3=50*a3
    c4=60*a4
    c5=40*a5
    c6=60*a6
    c7=20*a7
   
   
    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)
    
    Entry_Total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_Bill,bd=6,width=15,bg="lightgreen")
    Entry_Total.place(x=20,y=100)
    
    Totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %Totalcost)
    Total_Bill.set(string_bill)
   
Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menu Card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa..........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Idli..........Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Appe..........Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Noodles.......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="VeggieBurger......Rs.40",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="PaneerBurger......Rs.60",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="ColdDrinks.........Rs.20",fg="black",bg="lightgreen").place(x=10,y=230)


#bill
f2=Frame(root,bg="lightyellow",highlightbackground="Black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)
#Entry 
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Idli=StringVar()
Appe=StringVar()
Noodles=StringVar()
VeggieBurger=StringVar()
PaneerBurger=StringVar()
ColdDrinks=StringVar()
Total_Bill=StringVar()


#Label
lbl_Dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="purple")
lbl_Idli=Label(f1,font=("aria",20,'bold'),text="Idli",width=12,fg="purple")
lbl_Appe=Label(f1,font=("aria",20,'bold'),text="Appe",width=12,fg="purple")
lbl_Noodles=Label(f1,font=("aria",20,'bold'),text="Noodles",width=12,fg="purple")
lbl_VeggieBurger=Label(f1,font=("aria",20,'bold'),text="VeggieBurger",width=12,fg="purple")
lbl_PaneerBurger=Label(f1,font=("aria",20,'bold'),text="PaneerBurger",width=12,fg="purple")
lbl_ColdDrinks=Label(f1,font=("aria",20,'bold'),text="ColdDrinks",width=12,fg="purple")

lbl_Dosa.grid(row=1,column=0)
lbl_Idli.grid(row=2,column=0)
lbl_Appe.grid(row=3,column=0)
lbl_Noodles.grid(row=4,column=0)
lbl_VeggieBurger.grid(row=5,column=0)
lbl_PaneerBurger.grid(row=6,column=0)
lbl_ColdDrinks.grid(row=7,column=0)


#Entry
Entry_Dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
Entry_Idli=Entry(f1,font=("aria",20,'bold'),textvariable=Idli,bd=6,width=8,bg="lightpink")
Entry_Appe=Entry(f1,font=("aria",20,'bold'),textvariable=Appe,bd=6,width=8,bg="lightpink")
Entry_Noodles=Entry(f1,font=("aria",20,'bold'),textvariable=Noodles,bd=6,width=8,bg="lightpink")
Entry_VeggieBurger=Entry(f1,font=("aria",20,'bold'),textvariable=VeggieBurger,bd=6,width=8,bg="lightpink")
Entry_PaneerBurger=Entry(f1,font=("aria",20,'bold'),textvariable=PaneerBurger,bd=6,width=8,bg="lightpink")
Entry_ColdDrinks=Entry(f1,font=("aria",20,'bold'),textvariable=ColdDrinks,bd=6,width=8,bg="lightpink")

Entry_Dosa.grid(row=1,column=1)
Entry_Idli.grid(row=2,column=1)
Entry_Appe.grid(row=3,column=1)
Entry_Noodles.grid(row=4,column=1)
Entry_VeggieBurger.grid(row=5,column=1)
Entry_PaneerBurger.grid(row=6,column=1)
Entry_ColdDrinks.grid(row=7,column=1)


#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()