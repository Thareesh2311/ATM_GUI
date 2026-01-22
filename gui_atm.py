import tkinter as tk
from tkinter import messagebox
from datetime import datetime

balance = 100000
PIN = "1234"
transactions = []

def login():
    if pin_entry.get() == PIN:
        login_frame.pack_forget()
        atm_frame.pack()
    else:
        messagebox.showerror("Error", "Invalid PIN")

def check_balance():
    messagebox.showinfo("Balance", f"Your balance is ₹{balance}")

def deposit():
    global balance
    try:
        amount = int(amount_entry.get())
        if amount <= 0:
            raise ValueError
        balance += amount
        log_transaction(f"Deposited ₹{amount}")
        messagebox.showinfo("Deposit", f"₹{amount} deposited successfully. New balance is ₹{balance}")
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def withdraw():
    global balance
    try:
        amount = int(amount_entry.get())
        if amount <= 0:
            raise ValueError
        if amount > balance:
            messagebox.showerror("Error", "Insufficient Balance")
        else:
            balance -= amount
            log_transaction(f"Withdrawn ₹{amount}")
            messagebox.showinfo("Withdraw", f"₹{amount} withdrawn successfully. New balance is ₹{balance}")
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def log_transaction(message):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    transactions.append(f"{time} - {message}")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Transaction History")
    history_window.geometry("450x300")

    text = tk.Text(history_window)
    text.pack(fill=tk.BOTH, expand=True)

    if transactions:
        for t in transactions:
            text.insert(tk.END, t + "\n")
    else:
        text.insert(tk.END, "No transactions yet.")

    text.config(state=tk.DISABLED)

def logout():
    atm_frame.pack_forget()
    pin_entry.delete(0, tk.END)
    login_frame.pack()

root = tk.Tk()
root.title("ATM System")
root.geometry("400x350")
root.resizable(False, False)

login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="ATM LOGIN", font=("Arial", 18, "bold")).pack(pady=20)
tk.Label(login_frame, text="Enter PIN").pack()
pin_entry = tk.Entry(login_frame, show="*", width=20)
pin_entry.pack(pady=5)

tk.Button(login_frame, text="Login", width=15, command=login).pack(pady=10)

atm_frame = tk.Frame(root)

tk.Label(atm_frame, text="ATM MENU", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(atm_frame, text="Enter Amount").pack()
amount_entry = tk.Entry(atm_frame, width=25)
amount_entry.pack(pady=5)

tk.Button(atm_frame, text="Check Balance", width=20, command=check_balance).pack(pady=3)
tk.Button(atm_frame, text="Deposit", width=20, command=deposit).pack(pady=3)
tk.Button(atm_frame, text="Withdraw", width=20, command=withdraw).pack(pady=3)
tk.Button(atm_frame, text="Transaction History", width=20, command=show_history).pack(pady=3)
tk.Button(atm_frame, text="Logout", width=20, command=logout).pack(pady=10)

root.mainloop()
