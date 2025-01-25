import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL
)
""")
conn.commit()

# Function to add an expense
def add_expense():
    date = entry_date.get()
    category = combo_category.get()
    amount = entry_amount.get()

    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        amount = float(amount)
        cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))
        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully!")
        entry_date.delete(0, tk.END)
        combo_category.set("")
        entry_amount.delete(0, tk.END)
        update_table()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount!")

# Function to update the table
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT id, date, category, amount FROM expenses")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Function to generate a pie chart
def show_chart():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    if not data:
        messagebox.showinfo("No Data", "No expenses to display!")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.show()

# Function to delete all expenses
def clear_expenses():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all expenses?"):
        cursor.execute("DELETE FROM expenses")
        conn.commit()
        update_table()
        messagebox.showinfo("Success", "All expenses cleared!")

# Tkinter Setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x600")
root.configure(bg="lightblue")

# Title
label_title = tk.Label(root, text="Expense Tracker", font=("Arial", 18, "bold"), bg="lightblue")
label_title.pack(pady=10)

# Input Frame
frame_input = tk.Frame(root, bg="lightblue")
frame_input.pack(pady=10)

label_date = tk.Label(frame_input, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="lightblue")
label_date.grid(row=0, column=0, padx=5, pady=5)
entry_date = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_date.grid(row=0, column=1, padx=5, pady=5)

label_category = tk.Label(frame_input, text="Category:", font=("Arial", 12), bg="lightblue")
label_category.grid(row=1, column=0, padx=5, pady=5)
combo_category = ttk.Combobox(frame_input, values=["Food", "Transport", "Entertainment", "Bills", "Other"], state="readonly", font=("Arial", 12))
combo_category.grid(row=1, column=1, padx=5, pady=5)

label_amount = tk.Label(frame_input, text="Amount:", font=("Arial", 12), bg="lightblue")
label_amount.grid(row=2, column=0, padx=5, pady=5)
entry_amount = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_amount.grid(row=2, column=1, padx=5, pady=5)

btn_add = tk.Button(frame_input, text="Add Expense", font=("Arial", 12, "bold"), bg="darkblue", fg="white", command=add_expense)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

# Table Frame
frame_table = tk.Frame(root, bg="lightblue")
frame_table.pack(pady=10)

tree = ttk.Treeview(frame_table, columns=("ID", "Date", "Category", "Amount"), show="headings", height=10)
tree.column("ID", width=50, anchor="center")
tree.column("Date", width=150, anchor="center")
tree.column("Category", width=150, anchor="center")
tree.column("Amount", width=100, anchor="center")
tree.heading("ID", text="ID")
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.pack(side="left", padx=10)

scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Buttons Frame
frame_buttons = tk.Frame(root, bg="lightblue")
frame_buttons.pack(pady=20)

btn_chart = tk.Button(frame_buttons, text="Show Chart", font=("Arial", 12, "bold"), bg="green", fg="white", command=show_chart)
btn_chart.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(frame_buttons, text="Clear All Expenses", font=("Arial", 12, "bold"), bg="red", fg="white", command=clear_expenses)
btn_clear.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_buttons, text="Exit", font=("Arial", 12, "bold"), bg="gray", fg="white", command=root.quit)
btn_exit.grid(row=0, column=2, padx=10)

# Initialize Table
update_table()

# Footer
label_footer = tk.Label(root, text="Created with ❤️by Husem", font=("Arial", 10), bg="lightblue")
label_footer.pack(side="bottom", pady=10)

root.mainloop()
