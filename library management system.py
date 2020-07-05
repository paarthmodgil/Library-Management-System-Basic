######CREATE A DICTIONARY#####
library = dict() 
library = {'Networking':10,"Python":20, 
           "Cybersecurity":5}

####
def print_library():
    print(library)
    

 
####
def add_book(book_name, num_of_copies):
    library[book_name]= num_of_copies
    
####
def delete_book(book_name):
    library.pop(book_name)
    
####   
def update_copies(book_name, extra_copies):
    library[book_name]= library[book_name] + extra_copies

####
def check_availability(book_name):
    if book_name in library.keys() and library[book_name]>0:
        return True 
    else:
        return False
    
####
def issue_book (book_name):
    if check_availability(book_name):
        library[book_name] = library[book_name]-1
        print(book_name , "is issued")
    else:
        print('Book is unavailable currently')
   
####
def return_book(book_name):
    library[book_name] = library[book_name]+1
    print(book_name, " returned")
####
def search_book(book_name):
    if book_name in library.keys():
        print(book_name ,'is available')
    else:
        print("Book unavailable")


#### Main Function ####
if __name__ == '__main__':
    add_book('DBMS', 14)
    update_copies('Python', 10)
    issue_book('Cybersecurity')
    issue_book('Cybersecurity')
    issue_book('Cybersecurity')
    issue_book('Cybersecurity')
    issue_book('Cybersecurity')
    issue_book('Cybersecurity')
    return_book('Cybersecurity')
    issue_book('Cybersecurity')
    search_book ('Python')
    print(library)
    
    