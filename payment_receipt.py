from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas

def generate_receipt(name_entry,amount_entry,receipt_entry):
    c=canvas.Canvas(f"receipt_{receipt_entry}.pdf",)
   
    c.drawString(100,750, f"Receipt Number:{receipt_entry}")
    c.drawString(100,730, f"Name:{name_entry}")
    c.drawString(100,710, f"Amount Paid:{amount_entry}")
    c.drawString(100,690, f"Thank You for Payment!")
    c.save()
    messagebox.showinfo("Success", f"Receipt {receipt_entry} generated successfully!")



def submit():
    name_entry=name_var.get()
    amount_entry=amount_var.get()
    receipt_entry=number_var.get()

    if not name_entry:
        messagebox.showerror("Error","All Feild Must Be Required!")
    elif not amount_entry:
        messagebox.showerror("Error","All Feild Must Be Required!")
    elif not receipt_entry:
        messagebox.showerror("Error","All Feild Must Be Required!")
        return

    try:
        amount_entry=float(amount_entry)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    generate_receipt(name_entry,amount_entry,receipt_entry)

root=Tk()
root.title("PAYMENT RECEIPT")
name_var=StringVar()
amount_var=StringVar()
number_var=StringVar()

name=Label(root,text="Name:").grid(row=1,column=1,padx=10,pady=10)
en=Entry(root,textvariable=name_var).grid(row=1,column=2,padx=10,pady=10)

amount=Label(root,text="Amount:").grid(row=2,column=1,padx=10,pady=10)
ea=Entry(root,textvariable=amount_var).grid(row=2,column=2,padx=10,pady=10)

receipt_num=Label(root,text="Receipt Number:").grid(row=3,column=1,padx=10,pady=10)
er=Entry(root,textvariable=number_var).grid(row=3,column=2,padx=10,pady=10)

generate_receipt_BUTTON=Button(root,text="Generate Receipt",command=submit).grid(row=4,columnspan=3,pady=10)
root.mainloop()