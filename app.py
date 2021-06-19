import tkinter as tk
import tkcalendar as calendar
from tkinter import scrolledtext
from tkinter import messagebox
root=tk.Tk()
 
root.geometry("400x380")
root.resizable(False,False)

name_var=tk.StringVar()
mob_var=tk.StringVar()
 
def submit():
    f = open('data.txt', 'a')
 
    name=name_var.get()
    mob=mob_var.get()
    add=add_entry.get('1.0', tk.END)
    calval=cal.get_date()

    if len(mob) == 10:
        data = 'Name : ' + name + '\nMobile Number : ' + mob + '\nAddress : \n' + add + 'Date of Birth : ' + calval + ' \n\n'
        print(data)

        f.write(data)
        
        name_var.set("")
        mob_var.set("")
        add_entry.delete('1.0', tk.END)

        f.close()
    
    else:
        messagebox.showinfo("!", "Enter a valid Mobile Number!")     

name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
mob_label = tk.Label(root, text = 'Mobile Number', font = ('calibre',10,'bold'))
mob_entry=tk.Entry(root, textvariable = mob_var, font = ('calibre',10,'normal'))

add_label = tk.Label(root, text = 'Address', font = ('calibre',10,'bold'))
add_entry=scrolledtext.ScrolledText(root, wrap=tk.WORD,width=30,height=5,font=('calibre', 10,'normal'))

cal_label = tk.Label(root, text = 'Date of Birth', font = ('calibre',10,'bold'))
cal = calendar.Calendar(root, selectmode = 'day',year = 1990, month = 1,day = 1)
  
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
mob_label.grid(row=1,column=0)
mob_entry.grid(row=1,column=1)
add_label.grid(row=2,column=0)
add_entry.grid(row=2,column=1)
cal_label.grid(row=3,column=0)
cal.grid(row=3,column=1)
sub_btn.grid(row=4,column=1)

root.mainloop()