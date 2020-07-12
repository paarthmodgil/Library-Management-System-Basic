import datetime

class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = {} #dictionary
        self.issued_books = {} #dictionary        
    
    def print_all_books(self):
        for book, copies in self.books.items():
            print(book.name, book.ISBN, book.Author)
            

    
class Book:
    def __init__(self, name, ISBN, Author):
        self.name = name
        self.ISBN = ISBN
        self.Author = Author
        
    def print_all_details(self):
        print(self.name, self.ISBN, self.Author)
        


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        #books = {book_name: issue_date}
        self.books = {}

    def print_all_my_books(self):
        for book in self.books.keys():
            print(book.name)
            
        
                
class Librarian:
    
    def __init__(self, name, library):  
        self.name = name
        self.library = library
    
    def add_book(self, book, copies):
        #{book_name: num_of_copies}
        if book in self.library.books.keys():
            return 'BOOK ALREADY EXISTS'
        else:
            self.library.books[book] = copies
        
    def issue_book( self, book, student, date):
        for lb in self.library.books.keys():
            if lb.name == book.name:
                self.library.books[lb] -= 1
                student.books[book] = date            
            else:
                return 'BOOK UNAVAILABLE'


        
if __name__ == '__main__':
    St_Xaviers_Library = Library('St_Xaviers_Library')
    print(St_Xaviers_Library.print_all_books())
    
   
    
    Miss_Briganza = Librarian('Miss_Briganza', St_Xaviers_Library)

    
    book1 = Book('Romeo and Juliet', 'T6JSS','Shakespeare')
    book2 = Book('Harry Potter', "SAW77", 'J.K. Rowling')
    book3 = Book("Quantitative Aptitude", "GAM875", "R. S. Aggarwal")
    book4 = Book("Concepts of Physics", "LSG3723", "H. C. Verma")
    
    #book2.print_all_details()
    #ook1.print_all_details()
    #print_all_details(book1)
    
    Miss_Briganza.add_book(book1, 10)
    St_Xaviers_Library.print_all_books()
    
    rahul = Student('rahul', 3)
    anjali = Student("anjali", 1)
    tina = Student("tina", 1)

    
    Miss_Briganza.issue_book(book1, rahul, datetime.date(2020,7,1))
    Miss_Briganza.issue_book(book3, tina, datetime.date(2020,5,3))
    
    St_Xaviers_Library.print_all_books()
    rahul.print_all_my_books()