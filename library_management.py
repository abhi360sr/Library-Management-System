import sys


class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies


class BorrowedBook(Book):
    def __init__(self, title, author, isbn, username, userid):
        super().__init__(title, author, isbn, 1)  
        self.username = username
        self.userid = userid


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self):
        title = input("Enter the name of the book: ")
        author = input("Enter the author's name: ")
        isbn = input("Enter the ISBN: ")
        try:
            copies = int(input("Enter the number of copies: "))
            for b in self.books:
                if b.isbn == isbn:
                    b.copies += copies
                    print("Copies updated.")
                    return
            self.books.append(Book(title, author, isbn, copies))
            print("Book added successfully.")
        except ValueError:
            print("Invalid input. Number of copies must be an integer.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Copies: {book.copies}")

    def borrow_book(self):
        title = input("Enter the name of the book you want to borrow: ")
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                print("Book is available.")
                username = input("Enter your name: ")
                userid = input("Enter your User ID: ")
                book.copies -= 1
                self.borrowed_books.append(BorrowedBook(book.title, book.author, book.isbn, username, userid))
                print(f"Book borrowed successfully by {username}.")
                return
        print("Book is not available or out of stock.")

    def display_borrowed_books(self, book_name):
        print(f"\nBorrowed details for '{book_name}':")
        found = False
        for borrowed in self.borrowed_books:
            if borrowed.title.lower() == book_name.lower():
                print(f"Username: {borrowed.username}, User ID: {borrowed.userid}")
                found = True
        if not found:
            print("No one has borrowed this book.")

    def menu(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Add a Book")
            print("2. Borrow a Book")
            print("3. Display All Books")
            print("4. View Borrowed Book Details")
            print("5. Exit")
            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.borrow_book()
                elif choice == 3:
                    self.display_books()
                elif choice == 4:
                    book_name = input("Enter the book name: ")
                    self.display_borrowed_books(book_name)
                elif choice == 5:
                    print("Exiting the library system.")
                    sys.exit()
                else:
                    print("Invalid option. Please select again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    library = Library()
    library.menu()
