class Book():
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        

    def get_book_info(self):
        return "Title: {0}, Author: {1}, Price: {2}.".format(self.title,self.author,self.price)

 
def get_total_price(books_list):
    return sum([book.price for book in books_list])   

description = "This is a module named bookstore."