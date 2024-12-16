class Library:

    def __init__(self, listofbooks,name):
        self.list = listofbooks
        self.name = name
        self.lendDict = {}

    def DisplayBook(self):
        print("We have the following books at ou library:" , self.name)
        for book in listofbooks:
            print(book)

    def lendbook(self,name,user):
        if book not in self.listofbooks:
            print("Sorry, we do not have that book")

        elif book in self.lendDict:
            print("This book is already in use")

        else:
            self.lendDict[book] = user
            print("Lend Dictionary updated")


    def addbook(self,book):
        self.listofbooks.append(book)
        print({book},"has been added to our library")

    def returnbook(self,book):
        if book in self.lendDict:
            print("Thank you for returning this book")
            del self.lendDict[book]

        else:
            print("This book wasnt borrowed from us")



if __name__ == '__main__':
    books = Library(['C++ Basics' , 'Harry Potter' , 'Python' , 'Javascript' ],"Lets Upskill")
    user_input = input("Welcome to our library! What is your name?")


    while True :
        print("\r Welcome{user_name} to {self.name} Library")
        print("What would you like to do?\n1.Display books\n2.Lend books\n3.add books\n4.return books")
        user_input = input("Please choose an option ")

        if user_choice not in ['1', '2', '3', '4', '5']:

            print("Please enter a valid option.")
            continue

        if user_choice == '1':

            books.displayBooks()

        elif user_choice == '2':

            book = input("Enter the name of the book you want to lend: ")

            books.lendBook(user_name, book)

        elif user_choice == '3':

            book = input("Enter the name of the book you want to add: ")

            books.addBook(book)

        elif user_choice == '4':

            book = input("Enter the name of the book you want to return: ")

            books.returnBook(book)

        elif user_choice == '5':

            print(f"Thank you for using the library, {user_name}. Goodbye!")

            break




        
