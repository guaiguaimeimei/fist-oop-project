class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def display_info(self):
        ststus="已借阅" if self.is_borrowed else "可借阅"
        print(f'《{self.title}》|作者：{self.author}|状态：{ststus}')


if __name__=="__main__":
    book1=Book("Python入门","李教授")
    book2=Book('算法图解','王工程')
    book1.display_info()
    book1.is_borrowed=True
    book1.display_info()

class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f'成功入库：《{book.title}》')
    def list_books(self):
        print("\n======图书馆藏书=======")
        for book in self.books:
            book.display_info()

if __name__=="__main__":
    lib=library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.list_books()


