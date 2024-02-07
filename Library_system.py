class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = {"title": title, "author": author, "isbn": isbn}
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Library Books:")
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

    def update_book(self, title, new_title, new_author, new_isbn):
        for book in self.books:
            if book["title"].lower() == title.lower():
                book["title"] = new_title
                book["author"] = new_author
                book["isbn"] = new_isbn
                print(f"Book '{title}' updated.")

    def delete_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' deleted from the library.")
                return
        print(f"Book '{title}' not found in the library.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Display All Books")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")


        if choice == "1":
            while True:
                title = input("Enter the title: ")
                author = input("Enter the author: ")
                isbn = input("Enter the ISBN: ")
                library.add_book(title, author, isbn)
                add_other_books = input('Do you want to add another book:')
                if add_other_books != 'yes':
                    break



        elif choice == "2":
            title = input("Enter the title to search: ")
            search_result = library.search_book(title)
            if search_result:
                print(f"Found: {search_result}")
            else:
                print("Book not found.")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            title = input("Enter the title to update: ")
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author: ")
            new_isbn = input("Enter the new ISBN: ")
            library.update_book(title, new_title, new_author, new_isbn)

        elif choice == "5":
            title = input("Enter the title to delete: ")
            library.delete_book(title)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
