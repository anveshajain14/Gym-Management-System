import tkinter as tk
from tkinter import ttk, messagebox

existing_members = []

def member_exists(member_id):
    for member in existing_members:
        if member["member_id"] == member_id:
            return True
    return False

def add_member():
    member_id = member_id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    contact = contact_entry.get()
    
    if member_id and name and age and contact:
        existing_members.append({
            "member_id": member_id,
            "name": name,
            "age": age,
            "contact": contact,
        })
        messagebox.showinfo("Success", "Member added successfully")
        member_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all member details.")

def view_members():
    members_window = tk.Toplevel()
    members_window.title("All Members")

    members_table = ttk.Treeview(members_window, columns=("Member ID", "Name", "Age", "Contact"), show="headings")
    members_table.heading("Member ID", text="Member ID")
    members_table.heading("Name", text="Name")
    members_table.heading("Age", text="Age")
    members_table.heading("Contact", text="Contact")

    for member in existing_members:
        members_table.insert("", "end", values=(member["member_id"], member["name"], member["age"], member["contact"]))

    members_table.pack()

root = tk.Tk()
root.title("Gym Management System")

member_frame = tk.Frame(root, padx=10, pady=10)
member_frame.pack()

member_id_label = tk.Label(member_frame, text="Member ID:")
member_id_label.pack()
member_id_entry = tk.Entry(member_frame)
member_id_entry.pack()

name_label = tk.Label(member_frame, text="Name:")
name_label.pack()
name_entry = tk.Entry(member_frame)
name_entry.pack()

age_label = tk.Label(member_frame, text="Age:")
age_label.pack()
age_entry = tk.Entry(member_frame)
age_entry.pack()

contact_label = tk.Label(member_frame, text="Contact:")
contact_label.pack()
contact_entry = tk.Entry(member_frame)
contact_entry.pack()

add_member_button = tk.Button(member_frame, text="Add Member", command=add_member)
add_member_button.pack()

view_members_button = tk.Button(member_frame, text="View Members", command=view_members)
view_members_button.pack()

exit_button = tk.Button(member_frame, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()
