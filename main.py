"""
This program keeps track of all of our books
version : 1.0.0
Author : Bek Brace
Date :27.03.2020
PEP8 -- > check online 
"""


def main():
    # Initializing books list and invoking sotred data
    try:
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close
    except FileNotFoundError:
        print("theBooksList.txt not found")
        print("Starting a new Books List")
        booksList = []

    choice = 0
    while choice != 4:
        print("Books Manager")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>>")
            nAuthor = input("Enter the name of the author >>>")
            nPages = input("Enter the number of pages >>>")
            booksList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter search term >>>")
            for book in booksList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for x in range(len(booksList)):
                print(booksList[x])

        elif choice == 4:
            print("Quitting program")
    print("Program terminated")

    # Saving to external txt file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


main()
