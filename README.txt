
Personal Expense Tracker – README

@@@Description:
This is a beginner-level Python command-line application to track and manage personal daily expenses. It allows users to:

 1.Add new expenses
 2.View all recorded expenses
 3.Search expenses by category
 4.View a monthly expense summary

All data is stored in a text file named 'expenses.txt'.


@@@ How to Run:

1. Open a terminal or command prompt.
2. Navigate to the folder containing 'expense_tracker.py'.
3. Run the program using:
   python expense_tracker.py

@@@ Main Menu Options:

1. Add New Expense
   Input the date (YYYY-MM-DD), category, amount (float), and a description (optional).  
   This is saved to 'expenses.txt'.

2. View All Expenses
   Displays all recorded expenses in a neat table format.

3. Search by Category
   Enter a category (Food or Transport) to view only expenses under that category and see the total spent.

4. Monthly Summary
   Input a month in YYYY-MM format to get:
    # Total number of expenses
    # Total amount spent
    # Highest and lowest single expenses in that month

5. Exit
   Ends the program.

@@@ File Format ('expenses.txt'):
Each line represents an expense in this format:
YYYY-MM-DD|Category|Amount|Description

Example:
2025-05-01|Food|120.50|Lunch at cafe

@@@ Error Handling:
# If a non-numeric value is entered for the amount, an error message is shown.
# If the file is missing or corrupted, appropriate messages are displayed.
# Simple validation is done for the date and inputs.
