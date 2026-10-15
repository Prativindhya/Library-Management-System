# Library Management System

A simple command-line application written in **Python** to manage library books. It replaces slow, error-prone manual record keeping with an easy menu-driven program for adding books, searching for them, and tracking whether they are available or issued.

Made as a Class XI Computer Science / Informatics Practices project at Lotus Valley International School, Gurugram (2024-25).

## Features

- **Add books**: store a book's ID, title, author and year of publication
- **Remove books**: delete a book from the library records
- **Check availability**: see whether a book is available or issued
- **Search books**: look up a book's details by its ID
- **Issue books**: mark an available book as issued
- **Return books**: mark an issued book as available again

## Requirements

- Python 3 (no extra libraries needed)

## How to Run

```bash
python library_management_system.py
```

## Usage

The program shows a menu:

```
Library Management System:
1. Add Book
2. Remove Book
3. Check Availability
4. Search Book
5. Issue Book
6. Return Book
7. Exit
```

Enter the number of the option you want and follow the prompts. Book IDs are whole numbers.

### Example

```
Enter your choice: 1
Enter book ID: 1234
Enter book title: How To Kill A Mockingbird
Enter author: Harper Lee
Enter year of publication: 1962
Book 'How To Kill A Mockingbird' added.
```

## How It Works

Books are stored in a Python dictionary keyed by book ID, with each book holding its title, author, year and availability status. A second dictionary tracks which books are currently issued. Data is kept in memory, so it resets each time the program closes.

## Future Scope

- Printing book reports and receipts
- Modules for book reservations and tracking fines
- Hosting on an online server for access from anywhere
- Regular data backups
- Chat or messaging between users and staff
- Online book reservation
