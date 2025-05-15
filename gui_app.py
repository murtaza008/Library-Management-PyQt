# gui_app_pyqt.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton, QMessageBox, QListWidget, QCheckBox, QInputDialog
)
from book_library import Book, EBook, Library, BookNotAvailableError

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.library = Library()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Library Management System (PyQt5)")
        self.setGeometry(100, 100, 600, 600)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.size_input = QLineEdit()
        self.ebook_checkbox = QCheckBox("eBook?")
        self.ebook_checkbox.stateChanged.connect(self.toggle_size_input)

        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Author:"))
        layout.addWidget(self.author_input)
        layout.addWidget(QLabel("ISBN:"))
        layout.addWidget(self.isbn_input)
        layout.addWidget(self.ebook_checkbox)
        layout.addWidget(QLabel("Download Size (MB):"))
        layout.addWidget(self.size_input)
        self.size_input.setDisabled(True)

        self.listbox = QListWidget()
        layout.addWidget(self.listbox)

        # Buttons
        btns = QHBoxLayout()
        for text, method in [
            ("Add Book", self.add_book),
            ("Lend Book", self.lend_book),
            ("Return Book", self.return_book),
            ("Remove Book", self.remove_book),
            ("Books by Author", self.view_by_author)
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(method)
            btns.addWidget(btn)

        layout.addLayout(btns)
        self.setLayout(layout)
        self.update_book_list()

    def toggle_size_input(self):
        self.size_input.setEnabled(self.ebook_checkbox.isChecked())
        if not self.ebook_checkbox.isChecked():
            self.size_input.clear()

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()
        is_ebook = self.ebook_checkbox.isChecked()
        size = self.size_input.text()

        if not title or not author or not isbn:
            QMessageBox.warning(self, "Error", "All fields except size are required.")
            return

        if is_ebook:
            try:
                size = float(size)
                book = EBook(title, author, isbn, size)
            except ValueError:
                QMessageBox.warning(self, "Error", "Size must be a number.")
                return
        else:
            book = Book(title, author, isbn)

        self.library.add_book(book)
        QMessageBox.information(self, "Success", f"Book '{title}' added.")
        self.update_book_list()

    def lend_book(self):
        isbn, ok = QInputDialog.getText(self, "Lend Book", "Enter ISBN:")
        if ok:
            try:
                self.library.lend_book(isbn)
                QMessageBox.information(self, "Success", "Book lent.")
            except BookNotAvailableError as e:
                QMessageBox.warning(self, "Error", str(e))
        self.update_book_list()

    def return_book(self):
        isbn, ok = QInputDialog.getText(self, "Return Book", "Enter ISBN:")
        if ok:
            try:
                self.library.return_book(isbn)
                QMessageBox.information(self, "Success", "Book returned.")
            except BookNotAvailableError as e:
                QMessageBox.warning(self, "Error", str(e))
        self.update_book_list()

    def remove_book(self):
        isbn, ok = QInputDialog.getText(self, "Remove Book", "Enter ISBN:")
        if ok:
            self.library.remove_book(isbn)
            QMessageBox.information(self, "Removed", "Book removed.")
        self.update_book_list()

    def view_by_author(self):
        author, ok = QInputDialog.getText(self, "Author", "Enter author name:")
        if ok:
            books = list(self.library.books_by_author(author))
            self.listbox.clear()
            if books:
                self.listbox.addItem(f"Books by {author}:")
                for book in books:
                    self.listbox.addItem(str(book))
            else:
                self.listbox.addItem("No books found.")

    def update_book_list(self):
        self.listbox.clear()
        self.listbox.addItem("Available Books:")
        for book in self.library:
            self.listbox.addItem(str(book))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec_())
