# Library-Management-PyQt

A modern desktop Library Management System built with Python and PyQt5. Manage physical books and eBooks through an intuitive and responsive GUI.

## Features

- Add physical books and eBooks (with download size)
- Lend and return books with availability checks
- Remove books by ISBN
- Search books by author
- View real-time inventory of available books

## Technologies

- Python 3.x
- PyQt5 for GUI
- Custom exception handling

## Project Structure

Library-Management-PyQt/
├── book_library.py # Core classes and custom exceptions
├── gui_app.py # PyQt5 GUI application
└── README.md # Project documentation

## Setup

Clone the repository:

```bash
git clone https://github.com/your-username/Library-Management-PyQt.git
cd Library-Management-PyQt
```

Create and activate a virtual environment:

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

Install dependencies:

```bash
pip install PyQt5
```

## Usage

Run the application:

```bash
python gui_app.py
```

## Future Enhancements

- Persistent data storage (file or database)
- User authentication and lending history
- Advanced search and filtering
- Support for multiple copies per book
