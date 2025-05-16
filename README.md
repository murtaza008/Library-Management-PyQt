# 📘 Library-Management-PyQt

A modern desktop Library Management System built with **Python** and **PyQt5**. Manage physical books and eBooks with an intuitive graphical user interface.

---

## ✨ Features

- ➕ Add physical books and eBooks (with download size)
- 📤 Lend and 📥 return books with availability checks
- ❌ Remove books using ISBN
- 🔍 Search books by author name
- 📚 View real-time inventory of all books
- ⚠️ Custom exception handling for unavailable books

---

## 🖥️ Technologies Used

- Python 3.x  
- PyQt5 for GUI  
- Object-Oriented Programming (OOP)  
- Custom Exception Handling  

---

## 📂 Project Structure

```
Library-Management-PyQt/
│
├── book_library.py # Core classes: Book, EBook, Library, Exceptions
├── gui_app.py # GUI built with PyQt5
└── README.md # Project documentation
```

---

## ⚙️ Setup Instructions

## Create & Activate Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```
---

## Install Dependencies

```bash
pip install PyQt5
```
---

## ▶️ Run the Application

```bash
python gui_app.py
```
