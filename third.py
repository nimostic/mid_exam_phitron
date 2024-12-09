class Library:
    book_list = []
    @classmethod
    def entry_book(self,book):
        self.book_list.append(book)
         
class Book:
    def __init__(self,book_id,title,author,availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        
        Library.entry_book(self)
    def __repr__(self):
       return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.availability}"
  
        
book1 = Book(1, "1984", "George Orwell", True)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", True)



print(Library.book_list)

