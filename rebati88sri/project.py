
import json
from datetime import datetime
from colorama import Fore, Style

USER_FILE = "users.json"

# ------------------ DATA PERSISTENCE ------------------
def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

# ------------------ CORE FUNCTIONS ------------------
def check_pin(entered_pin, correct_pin):
    return entered_pin == correct_pin

def check_balance(balance):
    return f"{Fore.CYAN}Your current balance is: ₹{balance:,.2f}{Style.RESET_ALL}"

def deposit(balance, amount, history):
    if amount <= 0:
        return balance, "Invalid deposit amount."
    balance += amount
    history.append(f"Deposited ₹{amount:,.2f} on {datetime.now()}")
    return balance, f"Deposit successful. New balance: ₹{balance:,.2f}"

def withdraw(balance, amount, history):
    if amount % 100 != 0:
        return balance, "Amount must be in multiples of ₹100."
    elif amount > balance - 500:
        return balance, "Insufficient funds. ₹500 minimum balance required."
    balance -= amount
    history.append(f"Withdrew ₹{amount:,.2f} on {datetime.now()}")
    return balance, f"Withdrawal successful. New balance: ₹{balance:,.2f}"

def change_pin(user_data, new_pin):
    user_data["pin"] = new_pin
    return "PIN changed successfully."

def print_history(history):
    return "\n".join(history) if history else "No transactions yet."

def currency_converter(inr_amount):
    rate_usd = 83.0  # Static exchange rate
    return f"USD equivalent: ${inr_amount / rate_usd:.2f}"

# ------------------ USER INTERFACE ------------------
def atm_menu():
    print(f"\n{Fore.YELLOW}--- ATM Menu ---{Style.RESET_ALL}")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Currency Converter")
    print("7. Exit")

def admin_menu():
    print(f"\n{Fore.MAGENTA}--- Admin Menu ---{Style.RESET_ALL}")
    print("1. View All Users")
    print("2. Add New User")
    print("3. Exit Admin Mode")

def main():
    users = load_users()
    print(f"{Fore.GREEN}-------- WORLD ATM SIMULATOR --------{Style.RESET_ALL}")
    username = input("Enter username: ").lower()

    if username == "admin":
        while True:
            admin_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                for u in users:
                    print(f"- {u}: ₹{users[u]['balance']} | PIN: {users[u]['pin']}")
            elif choice == "2":
                uname = input("Enter new username: ").lower()
                if uname in users:
                    print("User already exists.")
                else:
                    try:
                        pin = int(input("Enter 4-digit PIN: "))
                        users[uname] = {"pin": pin, "balance": 0, "history": []}
                        save_users(users)
                        print("User created successfully.")
                    except:
                        print("Invalid input.")
            elif choice == "3":
                break
            else:
                print("Invalid admin choice.")
        return

    if username not in users:
        print("User not found.")
        return

    pin_attempts = 3
    while pin_attempts > 0:
        try:
            entered_pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Invalid PIN format.")
            continue

        if check_pin(entered_pin, users[username]["pin"]):
            break
        else:
            pin_attempts -= 1
            print(f"Incorrect PIN. {pin_attempts} attempt(s) remaining.")
    else:
        print("Too many failed attempts. Account locked.")
        return

    user_data = users[username]
    balance = user_data["balance"]
    history = user_data["history"]

    while True:
        atm_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(check_balance(balance))
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance, msg = deposit(balance, amount, history)
                print(msg)
            except:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw (₹100 multiples): "))
                balance, msg = withdraw(balance, amount, history)
                print(msg)
            except:
                print("Invalid amount.")
        elif choice == "4":
            try:
                new_pin = int(input("Enter new 4-digit PIN: "))
                print(change_pin(user_data, new_pin))
            except:
                print("Invalid PIN.")
        elif choice == "5":
            print(print_history(history))
        elif choice == "6":
            print(currency_converter(balance))
        elif choice == "7":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    users[username]["balance"] = balance
    users[username]["history"] = history
    save_users(users)

if __name__ == "__main__":
    main()
