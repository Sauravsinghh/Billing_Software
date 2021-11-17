from tkinter import*
from tkinter import font
from typing import Counter

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="#07266C",fg="White",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        #---------------------------------------- Customer Detail ------------------------------------------------------------------------
        
        f1=LabelFrame(self.root,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg="#07266C")
        f1.place(x=0,y=80,relwidth=1)
        
        cname=Label(f1,text="Customer Name",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=30,pady=6)
        cname_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(f1,text=" Phone No.",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=30,pady=6)
        cphn_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(f1,text=" Bill Number",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=30,pady=6)
        c_bill_txt=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(f1,text="search",width=10,bd=7,font="arial 12 bold"). grid(row=0,column=6,padx=10, pady=10)
        
        
        
        #==========================================      Cosmetics Frame===============================================================================================================
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Cosmetics",font=("times new roman",15,"bold"),fg="gold")
        F2.place(x=5,y=180,width=325,height=380)
        
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        face_Wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        shampoo_lbl=Label(F2,text="Shampoo",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        shampoo_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        hair_Oil_lbl=Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_Oil_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lotion_lbl=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        #===========================================     Grocery Frame    ================================================================================================
              
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Grocery",font=("times new roman",15,"bold"),fg="gold")
        F3.place(x=335,y=180,width=325,height=380)
        
        food_oil_lbl=Label(F3,text="Bath Soap",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        food_oil_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        rice_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        sugar_lbl=Label(F3,text="Face Wash",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sugar_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        salt_lbl=Label(F3,text="Shampoo",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        salt_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        flour_lbl=Label(F3,text="Hair Oil",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        flour_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        spices_lbl=Label(F3,text="Body Lotion",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        spices_lbl=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        
        #==========================================      Snacks Frame     ==============================================================================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Snacks",font=("times new roman",15,"bold"),fg="gold")
        F4.place(x=670,y=180,width=325,height=380)
        
        cold_drink_lbl=Label(F4,text="Cold Drink",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cold_drink_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Pizza_lbl=Label(F4,text="Pizza",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        pizza_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        burger_lbl=Label(F4,text="Burger",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        burger_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        sweets_lbl=Label(F4,text="Sweets",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sweets_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        boos_lbl=Label(F4,text="Boos",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        boos_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        samosa_lbl=Label(F4,text="Samosa",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        samosa_lbl=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        #==========================================  Bill Printing Area    ==============================================================================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=345,height=380)
        bill_label=Label(F5,text="Bill area", font=("arial",18,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        
         #==========================================   Snacks Frame    ==============================================================================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Bill Menu",font=("times new roman",15,"bold"),fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1=Label(F6,text="Total Cosmatic Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F6,text="Total Grocery Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3=Label(F6,text="Total Snacks Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        m4=Label(F6,text="Cosmatic Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m4_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        m5=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m5_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        m6=Label(F6,text="Snacks Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m6_txt=Entry(F6,width=18,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        
        
        #======================================== Button Frame ============================================
        
        
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=730,width=595,height=105)
        
        total_btn=Button(btn_f,text="Total",bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)

        gbill_btn=Button(btn_f,text="Generate Bill",bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)

        clear_btn=Button(btn_f,text="Clear bill",bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        
        exit_btn=Button(btn_f,text="Exit",bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        

root=Tk() 
obj = Bill_App(root)
root.mainloop()
