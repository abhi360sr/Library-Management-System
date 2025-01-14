# Library Management System

A simple Python-based Library Management System that allows users to:
- Add books to the library.
- Borrow books if they are available.
- Display all available books in the library.
- View details of borrowed books.

This program uses object-oriented programming principles for efficient functionality and modularity.

---

## Features

1. **Add a Book**  
   Add books to the library with details such as:
   - Title
   - Author
   - ISBN
   - Number of copies  
   Duplicate books (based on ISBN) will have their copies updated.

2. **Borrow a Book**  
   Borrow a book from the library by providing the book title. If the book is available:
   - The user provides their name and ID to borrow it.
   - The available copies of the book are reduced by 1.

3. **Display All Books**  
   View a list of all available books in the library with details such as:
   - Title
   - Author
   - ISBN
   - Number of copies remaining

4. **View Borrowed Book Details**  
   Check who borrowed a specific book by entering the book title. If borrowed, it displays:
   - Username
   - User ID

5. **Exit**  
   Exit the program safely.

---

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Save the code in a file named `library_management.py`.
3. Run the program using the command:
   ```bash
   python library_management.py
