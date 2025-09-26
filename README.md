🏦 Sethi Bank – GUI Banking System

A Python-based Bank Management System with GUI built using Tkinter.
This project simulates basic banking operations like account creation, deposit, withdrawal, deletion, and account viewing, with a clean GUI and CSV file-based storage.

✨ Features

🎨 Graphical User Interface using Tkinter

👤 Create and manage user accounts

💰 Perform deposits and withdrawals with receipts

🔑 Secure account authorization with password check

📑 View full account details (profile, address, DOB, balance)

❌ Delete accounts securely

🧾 Bill/receipt generation for each transaction

🗄️ CSV-based backend (no database required)

📂 Project Structure
bank-gui/
│── backgrounds/          # Background images for GUI
│── buttons/              # Button images
│── users/                # Stores transaction history per account
│── acount_list.csv       # Main CSV file with all account records
│── bank_gui.py           # Main project file (this script)

⚙️ How It Works

Home Screen → Options for Create, View, Edit, Delete, Deposit, Withdraw

Create Account → User enters details (name, DOB, phone, email, address, password). Data saved in acount_list.csv.

Deposit / Withdraw → Authenticate with account number & password, update balance, log transaction in users/<acc_no>.csv.

View Account → See all user details (non-editable).

Delete Account → Permanently remove account record from acount_list.csv.

Transaction Receipt → A separate receipt window is displayed for each deposit/withdraw.

🚀 Installation & Setup
Prerequisites

Python 3.7+

Tkinter (usually included with Python)

Clone Repo
git clone https://github.com/your-username/bank-gui.git
cd bank-gui

Run the App
python bank_gui.py

🖼️ Screenshots

👉 (Add your actual screenshots here — e.g., home screen, create account, deposit window, transaction bill)

🔮 Future Improvements

Switch from CSV → SQLite/MySQL database

Add account editing functionality

Better error handling (instead of popups only)

Password encryption for stronger security

Modernize GUI with Tkinter ttk themes or PyQt/PySide
