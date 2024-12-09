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
    def borrow_book(self):
        if self.availability == True:
            self.availability = False
            return True
        else :
            return False
        
book1 = Book(1, "1984", "George Orwell", True)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", True)

Library.entry_book(book1)
Library.entry_book(book2)


result = Book.borrow_book(book1)
print(result)
result2 = Book.borrow_book(book1)
print(result2)
