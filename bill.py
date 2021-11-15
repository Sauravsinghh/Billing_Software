from tkinter import*

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="#07266C",fg="White",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        #------------------------ Customer Detail ----------------------------------------
        
        f1=LabelFrame(self.root,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg="#07266C")
        f1.place(x=0,y=80,relwidth=1)
        
        cname=Label(f1,text="Customer Name",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=30,pady=6)
        

root=Tk()
obj = Bill_App(root)
root.mainloop()