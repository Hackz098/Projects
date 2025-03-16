import json
import os

# Constants
BOOKS_FILE = "books.json"

# Load existing books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book():
    books = load_books()
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN/Book ID: ").strip()
    genre = input("Enter genre: ").strip()
    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be positive values.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    for book in books:
        if book['isbn'] == isbn:
            print("Book with this ISBN already exists.")
            return
    
    books.append({"title": title, "author": author, "isbn": isbn, "genre": genre, "price": price, "quantity": quantity})
    save_books(books)
    print("Book added successfully.")

# View all books
def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    
    for book in books:
        print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nGenre: {book['genre']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")

# Remove a book
def remove_book():
    books = load_books()
    isbn = input("Enter ISBN/Book ID to remove: ").strip()
    books = [book for book in books if book['isbn'] != isbn]
    save_books(books)
    print("Book removed successfully.")

# Main menu
def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


