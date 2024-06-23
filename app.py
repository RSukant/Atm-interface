import tkinter as tk

class ATM(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.id = 123456789
        self.pin = 123456
        self.balance = 1000
        self.transaction_history = []
        self.create_widgets()

    def login(self):
        iid = int(self.id_entry.get())
        y = int(self.pin_entry.get())
        if iid == self.id and y == self.pin:
            self.login_label.config(text="Id and Pin is correct.")
            self.command_label.config(text="Enter command such as deposit, withdraw, transaction, history and quit.")
            self.command_entry.config(state="normal")
        else:
            self.login_label.config(text="Id or Pin is wrong. Please try again.")

    def process_command(self):
        command = self.command_entry.get()
        command = command.strip().lower()
        if command == "deposit":
            amount = int(self.amount_entry.get())
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            self.transaction_history.append(f"Balance: {self.balance}")
            self.output_text.insert("end", f"Successfully deposited. Balance: {self.balance}\n")
        elif command == "withdraw":
            amount = int(self.amount_entry.get())
            if amount > self.balance:
                self.output_text.insert("end", "Sorry no sufficient balance\n")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdraw: {amount}")
                self.transaction_history.append(f"Balance: {self.balance}")
                self.output_text.insert("end", f"Successfully withdrawed. Balance: {self.balance}\n")
        elif command == "transaction":
            amount = int(self.amount_entry.get())
            if amount > self.balance:
                self.output_text.insert("end", "Sorry no sufficient balance\n")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Transaction: {amount}")
                self.transaction_history.append(f"Balance: {self.balance}")
                self.output_text.insert("end", f"Successfully transaction. Balance: {self.balance}\n")
        elif command == "history":
            self.output_text.insert("end", "Transaction history\n")
            self.output_text.insert("end", "Initial balance: 1000\n")
            if not self.transaction_history:
                self.output_text.insert("end", "No transactions made yet.\n")
            else:
                for transaction in self.transaction_history:
                    self.output_text.insert("end", transaction + "\n")
        elif command == "quit":
            self.output_text.insert("end", "Thank you.\n")
            self.command_entry.config(state="disabled")
        else:
            self.output_text.insert("end", "Invalid command. Please try again.\n")

    def create_widgets(self):
        self.id_label = tk.Label(self, text="Enter ID:")
        self.id_label.pack(side="top")

        self.id_entry = tk.Entry(self)
        self.id_entry.pack(side="top")

        self.pin_label = tk.Label(self, text="Enter Pin:")
        self.pin_label.pack(side="top")

        self.pin_entry = tk.Entry(self, show="*")
        self.pin_entry.pack(side="top")

        self.login_button = tk.Button(self)
        self.login_button["text"] = "Login"
        self.login_button["command"] = self.login
        self.login_button.pack(side="top")

        self.login_label = tk.Label(self, text="")
        self.login_label.pack(side="top")

        self.command_label = tk.Label(self, text="")
        self.command_label.pack(side="top")

        self.command_entry = tk.Entry(self)
        self.command_entry.pack(side="top")
        self.command_entry.config(state="disabled")

        self.amount_label = tk.Label(self, text="Enter amount:")
        self.amount_label.pack(side="top")

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="top")

        self.process_button = tk.Button(self)
        self.process_button["text"] = "Process"
        self.process_button["command"] = self.process_command
        self.process_button.pack(side="top")

        self.output_text = tk.Text(self)
        self.output_text.pack(side="bottom")

root = tk.Tk()
app = ATM(master=root)
app.pack()
root.mainloop()
