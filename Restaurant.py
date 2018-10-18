from tkinter import *
import random
import time



root=Tk()
root.geometry("1600x800+0+0")
root.title("RESTAURANT MANAGEMENT SYSTEM")
text_input=StringVar()
operator=""

Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,bg="powder blue",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)


#==============for time==========================================
localtime=time.asctime(time.localtime(time.time()))

#====================================Info======================================================================

lblinfo=Label(Tops,font=('arial',50,'bold'),text="RESTAURANT MANAGEMENT SYSTEM",fg="Steel Blue",bd=10,anchor='w') # anchor tag is used for position
#grid used for automatic positioning, it is very easier than pack()
lblinfo.grid(row=0,column=0)

lblinfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblinfo.grid(row=1,column=0)

#******************************************Calculator*******************************************
def btnClick(numbers):
	global operator
	operator=operator+str(numbers)
	text_input.set(operator)

def clrDisplay():
	global operator
	operator=""
	text_input.set("")

def equals():
	global operator
	sumup=str(eval(operator))
	text_input.set(sumup)
	operator=""

def Ref():
	x=random.randint(12908,50876)
	randomRef=str(x)
	rand.set(randomRef)
	total1=int(Fries.get())+int(Burgur.get())+int(Filet.get())+int(Chicken.get())+int(Cheese.get())+int(Drinks.get())+int(CostOfMeals.get())+int(ServiceCharge.get())
	total2=total1+( int(StateTax.get())/100 * total1)
	SubTotal.set(str(total1))
	TotalCost.set(str(total2))


def qExit():
	root.destroy()

def Reset():
	rand.set("")
	Fries.set("")
	Burgur.set("")
	Filet.set("")
	Chicken.set("")
	Cheese.set("")
	Drinks.set("")
	CostOfMeals.set("")
	ServiceCharge.set("")
	StateTax.set("")
	SubTotal.set("")
	TotalCost.set("")



txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+"))
Addition.grid(row=2,column=3)
#========================================================================================================
btn4=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6))
btn6.grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-"))
Subtraction.grid(row=3,column=3)
#==========================================================================================================
btn1=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*"))
multiply.grid(row=4,column=3)

#=====================================================================================================================
btn0=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0))
btn0.grid(row=5,column=0)

btnC=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=lambda:clrDisplay())
btnC.grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=lambda:equals())
btnEquals.grid(row=5,column=2)

division=Button(f2,padx=16,pady=16, bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/"))
division.grid(row=5,column=3)

#================================================================================================================================
#----------------------------Restaurant Info1-----------------------------------------------------------------------------
rand=StringVar()
Fries=StringVar()
Burgur=StringVar()
Filet=StringVar()
Chicken=StringVar()
Cheese=StringVar()
Drinks=StringVar()
CostOfMeals=StringVar()
ServiceCharge=StringVar()
StateTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()




lblReference=Label(f1,font=('arial',16,'bold'),text='Reference',bd=16,anchor='w')
lblReference.grid(row=0,column=0)

txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text='Large Fries',bd=16,anchor='w')
lblFries.grid(row=1,column=0)

txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblBurgur=Label(f1,font=('arial',16,'bold'),text='Burgur Meal',bd=16,anchor='w')
lblBurgur.grid(row=2,column=0)

txtBurgur=Entry(f1,font=('arial',16,'bold'),textvariable=Burgur,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurgur.grid(row=2,column=1)


lblFilet=Label(f1,font=('arial',16,'bold'),text="Filet_o_Meal",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)

txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg="powder blue",justify="right")
txtFilet.grid(row=3,column=1)

lblchicken=Label(f1,font=('arial',16,'bold'),text='Chicken Meal',bd=16,anchor='w')
lblchicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtChicken.grid(row=4,column=1)


lblCheese=Label(f1,font=('arial',16,'bold'),text='Cheese Meal',bd=16,anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtCheese.grid(row=5,column=1)
#=============================================Restaurant info 2=============================================================

lblDrinks=Label(f1,font=('arial',16,'bold'),text='Drinks',bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)

txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCostOfMeals=Label(f1,font=('arial',16,'bold'),text='cost of meals',bd=16,anchor='w')
lblCostOfMeals.grid(row=1,column=2)

txtCostOfMeals=Entry(f1,font=('arial',16,'bold'),textvariable=CostOfMeals,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCostOfMeals.grid(row=1,column=3)


lblServiceCharge=Label(f1,font=('arial',16,'bold'),text='Service Charge',bd=16,anchor='w')
lblServiceCharge.grid(row=2,column=2)

txtServiceCharge=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceCharge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtServiceCharge.grid(row=2,column=3)



lblStateTax=Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)

txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=StateTax,bd=10,insertwidth=4,bg="powder blue",justify="right")
txtStateTax.grid(row=3,column=3)

lblSubTotal=Label(f1,font=('arial',16,'bold'),text='Sub Total',bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtSubTotal.grid(row=4,column=3)


lblTotalCost=Label(f1,font=('arial',16,'bold'),text='Total Cost',bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=TotalCost,bd=10,insertwidth=4,bg='powder blue',justify='right')
txtTotalCost.grid(row=5,column=3)

#=====================================Buttons=======================================

btnTotal=Button(f1,padx=16,pady=8,bd=16,text="Total",fg="black",font=('arial',16,'bold'),width=10,bg='powder blue',command=Ref).grid(row=7,column=1)


btnReset=Button(f1,padx=16,pady=8,bd=16,text="Reset",fg="black",font=('arial',16,'bold'),width=10,bg='powder blue',command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,text="Exit",fg="black",font=('arial',16,'bold'),width=10,bg='powder blue',command=qExit).grid(row=7,column=3)
if __name__=='__main__':
	root.mainloop()
