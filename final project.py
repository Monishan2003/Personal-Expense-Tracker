# Personal Expense Tracker
# This program allows users to manage daily expenses via a command-line interface.
# It supports adding, viewing, searching, and summarizing expenses stored in a text file.


file_name = 'expenses.txt'  

# Function to add a new expense entry
def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    try:
        amount = float(input("Amount: "))
    except:
        print("Invalid amount.\n")
        return
    desc = input("Description: ")
    try:
        with open(file_name, 'a') as file1:
            file1.write(f"{date}|{category}|{amount}|{desc}\n")
        print("Expense added.\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Function to display all expenses in a tabular format
def view_expenses():
    try:
        with open(file_name) as file1:
            print("\nDate       | Category   | Amount | Description")
            print("-" * 50)
            for line in file1:
                d, c, a, desc = line.strip().split('|')
                print(f"{d:10} | {c:10} | {a:6} | {desc}")
            print()
    except:
        print("No data found.\n")

# Function to filter expenses by category
def search_by_category():
    cat = input("Category to search: ")
    total = 0
    try:
        with open(file_name) as file1:
            for line in file1:
                d, c, a, desc = line.strip().split('|')
                if c.lower() == cat.lower():  # Case-insensitive match
                    print(f"{d:10} | {c:10} | {a:6} | {desc}")
                    total += float(a)
        print(f"Total: {total}\n")
    except:
        print("Error reading file.\n")

# Function to generate monthly summary
def monthly_summary(): 
    month = input("Enter YYYY-MM: ")
    total = count = 0
    high = low = None
    try:
        with open(file_name) as file1:
            for line in file1:
                d, c, a, desc = line.strip().split('|')
                if d.startswith(month):
                    a = float(a)
                    total += a
                    count += 1
                    if high is None or a > high: high = a
                    if low is None or a < low: low = a
        if count:
            print(f"Count: {count}, Total: {total}, High: {high}, Low: {low}\n")
        else:
            print("No records for that month.\n")
    except:
        print("Error reading file.\n")

# Main menu loop for interacting with the user
def main(): 
    while True:
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Monthly Summary")
        print("5. Exit")
        ch = input("Choose: ")
        if ch == '1': add_expense()
        elif ch == '2': view_expenses()
        elif ch == '3': search_by_category()
        elif ch == '4': monthly_summary()
        elif ch == '5': break  # Exit the program
        else: print("Invalid.\n")

# Entry point of the script
main()
