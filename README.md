# Expense Tracker with Tkinter

A simple Expense Tracker application built using Python, Tkinter for the GUI, SQLite for database storage, and Matplotlib for visualizations. This app allows users to log, view, and visualize their daily expenses in a clean and user-friendly interface.

## Screenshots
![image](https://github.com/user-attachments/assets/020e2740-fd51-48fc-b405-3157b5688e93)

## Features

- **Add Expenses**:
  - Log daily expenses with date, category, and amount.
  - Categories include Food, Transport, Entertainment, Bills, and Other.
- **View Expenses**:
  - Display all expenses in a scrollable table with columns for ID, Date, Category, and Amount.
- **Visualize Expenses**:
  - Generate a pie chart to see spending distribution by category.
- **Clear Expenses**:
  - Option to delete all logged expenses.
- **Persistent Data**:
  - Expenses are stored in an SQLite database for durability.
- **Error Handling**:
  - Validates input fields and prevents invalid data entry.

## Prerequisites

- Python 3.x installed on your system
- Required libraries:
  - `matplotlib` (Install via `pip install matplotlib`)
  - `sqlite3` (Comes pre-installed with Python)

## How to Run the App

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/expense-tracker-tkinter.git
   cd expense-tracker-tkinter
