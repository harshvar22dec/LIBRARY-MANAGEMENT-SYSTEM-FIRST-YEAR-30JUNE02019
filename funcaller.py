from funcdef import *
while True:
    print('''
        Welcome in Central Library
            Press S to search a book
             Press A to Add a new book
              Press C for Admin Services''')
    response=input().upper()
    if response=='S':
        search_by_name() if input('''Press A to search by name of author
        Otherwise default search is category-based\t''')=='A' else search_by_categ()
    elif response=='A':add_data()
    elif response=='C':admin_serv()
    else:print('Wrong Key Pressed!')
