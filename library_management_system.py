books = {}
issued_books = {}

while True:
    print("\nLibrary Management System:")
    print("1. Add Book\n2. Remove Book\n3. Check Availability\n4. Search Book\n5. Issue Book\n6. Return Book\n7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter book ID: "))
        if book_id not in books:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter year of publication: ")
            books[book_id] = {"title": title, "author": author, "year": year, "available": True}
            print(f"Book '{title}' added.")
        else:
            print("Book ID already exists.")

    elif choice == "2":
        book_id = int(input("Enter book ID to remove: "))
        if book_id in books:
            title = books[book_id]["title"]
            books.pop(book_id)
            issued_books.pop(book_id, None)
            print(f"Book '{title}' removed.")
        else:
            print("Book not found.")

    elif choice == "3":
        book_id = int(input("Enter book ID to check: "))
        if book_id in books:
            status = "Available" if books[book_id]["available"] else "Issued"
            print(f"Book '{books[book_id]['title']}' is {status}.")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = int(input("Enter book ID to search: "))
        if book_id in books:
            info = books[book_id]
            print(f"Found: {info['title']}, {info['author']}, {info['year']}")
        else:
            print("Book not found.")

    elif choice == "5":
        book_id = int(input("Enter book ID to issue: "))
        if book_id in books and books[book_id]["available"]:
            books[book_id]["available"] = False
            issued_books[book_id] = True
            print(f"Book '{books[book_id]['title']}' issued.")
        else:
            print("Book is either not found or already issued.")

    elif choice == "6":
        book_id = int(input("Enter book ID to return: "))
        if book_id in issued_books:
            books[book_id]["available"] = True
            issued_books.pop(book_id)
            print(f"Book '{books[book_id]['title']}' returned.")
        else:
            print("Book was not issued.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
