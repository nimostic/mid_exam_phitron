class Library:
    book_list = []
    @classmethod
    def entry_book(self,book):
        self.book_list.append(book)
         
class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        
        Library.entry_book(self)
        
    def borrow_book(self):
        
        if self.__availability:
            self.__availability = False
            print(f'Book : {self.__title} has been borrowed.')
            
        else :
            raise ValueError(f"Book : {self.__title} already borrowed")
        
    def return_book(self):
        if not self.__availability:
           self.__availability = True
        else :
            raise ValueError(f'{self.__title} is not borrowed.')

    def view_book_info(self):
            
            if self.__availability == True :
                book_available = 'Available'
                
            else:
                book_available = 'Borrowed'
            print(f"Book ID: {self.__book_id} \nTitle: {self.__title} \nAuthor: {self.__author}, \nAvailbility: {book_available}")
            print('\n') 
    
    def getbook_id(self):
        return self.__book_id
    
    
    
def menu():
      while True:
            print("\nMenu:")
            print("1. View All Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Exit")
            
            key = input('Enter Your Choice: ')
            print(key)
            if key=='1':
                
                if not Library.book_list:
                    print('This book is not available')
                else:
                    for book in Library.book_list:
                        book.view_book_info()
            elif key == '2':
                try:
                    book_id = input("Enter Book id to borrow: ")
                    for book in Library.book_list:
                        if book.getbook_id() == book_id:
                            book.borrow_book()
                            break
                    else:
                        raise ValueError('Invalid Book ID')
                except ValueError as e:
                    print(e)
                
            elif key == '3':
                try:
                    book_id = input("Enter Book id to return: ")
                    for book in Library.book_list:
                        if book.getbook_id() == book_id:
                            book.return_book()
                            break
                    else :
                        raise ValueError("No such book is exists.")
                except ValueError as e:
                    print(e)   
            elif key == '4':
                print('Exiting system.')
                break
            else:
                print('inavlid choice, plz try again.')

                

 
book1 = Book("110", "1984", "George Orwell", True)
book2 = Book("120", "Khuchi Mushi", "Harper Lee", True)
book3 = Book("130", "The Great Gatsby", "F. Scott Fitzgerald", True)
book4 = Book("140", "Chatar Matha", "Barrister Sumon", True)
book5 = Book("150", "To Kill a Mockingbird", "Sheikh Ahsina", True)

menu()