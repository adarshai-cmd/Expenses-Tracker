import json
import csv

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():

    date = input("Enter date (DD-MM-YYYY): ")

    categories = [
        "Food",
        "Travel",
        "Shopping",
        "Education",
        "Medical",
        "Bills",
        "Other"
    ]

    for category in categories:

        print("\n----------", category, "----------")

        item = input("Enter item/description: ")

        amount = float(input("Enter amount: "))

        if amount > 0:

            expense = {
                "date": date,
                "category": category,
                "item": item,
                "amount": amount
            }

            expenses.append(expense)

    save_expenses()

    print("\nExpense added successfully!")

    input("\nPress Enter to return to Main Menu...")

def view_expenses():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSE HISTORY ==========")

    for expense in expenses:

        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Item:", expense["item"])
        print("Amount: ₹", expense["amount"])
        print("--------------------------------")

def total_expenses():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expenses:", total)
   
def monthly_expenses():
        if len(expenses) == 0:
            print("\nNo expenses found.")
            return

        search_month = input("Enter month (MM-YYYY): ")

        total = 0

        for expense in expenses:

            month_year = expense["date"][3:]

            if month_year == search_month:
                total = total + expense["amount"]

        print("\nMonthly Expenses:", total)

def export_to_csv():

        if len(expenses) == 0:
            print("\nNo expenses found.")
            return

        with open("expenses.csv", "w", newline="") as file:

            fieldnames = ["date", "category", "item", "amount"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(expenses)

        print("\nExpenses exported successfully to expenses.csv")
        input("\nPress Enter to return to Main Menu...")

while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expense History")
        print("3. View Total Expenses")
        print("4. View monthly Expenses ")
        print("5. Export Expenses to CSV")
        print("6. Exit ")


        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            monthly_expenses()

        elif choice == "5":
            export_to_csv()
    
        elif choice == "6":
            print("\nThank you for using Expense Tracker!") 
            break

        else:
            print("Invalid choice! Please try again.")
