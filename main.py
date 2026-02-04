import csv

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    note = input("Enter note: ")
    print("Saved to", FILENAME)
    with open(FILENAME, "a", newline="") as f:

        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
    print("Expense added.")

def view_expenses():
    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.reader(f)
            print("\n--- All Expenses ---")
            empty = True
            for row in reader:
                if row:
                    print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Note: {row[3]}")
                    empty = False
            if empty:
                print("No expenses found.")
    except FileNotFoundError:
        print("No expenses found.")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0.0
    found = False

    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].startswith(month):
                    total += float(row[2])
                    found = True

        if found:
            print(f"Total expenses for {month}: {total}")
        else:
            print("No expenses found for this month.")
    except FileNotFoundError:
        print("No expenses found.")

def category_summary():
    totals = {}

    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    category = row[1]
                    amount = float(row[2])
                    totals[category] = totals.get(category, 0) + amount

        if not totals:
            print("No expenses found.")
            return

        print("\n--- Category Summary ---")
        for category, total in totals.items():
            print(f"{category}: {total}")

    except FileNotFoundError:
        print("No expenses found.")

def menu():
    while True:
        print("\n1. Add Expenses")
        print("2. View Expenses")
        print("3. Monthly Expenses")
        print("4. Category Summary")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "0":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    menu()