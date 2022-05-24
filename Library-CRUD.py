libraryDict={
    '9793062797':
        {
            'Title':'Laskar Pelangi',
            'Author':'Andrea Hirata',
            'Status':'Available',
            'Loc/Return Date':'Rak 1',
            'Borrower ID':'-'
        },
    '9780812981605':
        {
            'Title':'The Power of Habit',
            'Author':'Charles Duhigg',
            'Status':'Available',
            'Loc/Return Date':'Rak 2',
            'Borrower ID':'-'
        },
    '9780374533557':
        {
            'Title':'Thinking, Fast and Slow',
            'Author':'Daniel Kahneman',
            'Status':'Unavailable',
            'Loc/Return Date':'2 Juni 2022',
            'Borrower ID':'A001'
        },
    '9783161484100':
        {
            'Title':'Grit: The Power of Passion and Perseverance',
            'Author':'Angela Duckworth',
            'Status':'Unavailable',
            'Loc/Return Date':'4 Juni 2022',
            'Borrower ID':'A002'
        }
}

def mainShowBook():
    global libraryDict
    while True:
        print('\n'+' Show Book Information and Borrowing Status '.center(50,'-'),
        '\n1. Show [All] Book Information and Borrowing Status',
        '\n2. Show [Specific] Book Information and Borrowing Status',
        '\n3. Back')
        selectMenu=str(input('Select a Menu : '))
        if selectMenu=='1':
            if len(libraryDict)==0:
                print('No Data Available!')
            else:
                print('ISBN'.ljust(15),'|Title'.ljust(22),'|Author'.ljust(22),'|Status'.ljust(22),'|Location/Return Date'.ljust(22),'|Borrower ID'.ljust(22))
                for i in libraryDict:
                    print(f'{i}\t',end='')
                    for j in libraryDict[i]:
                        print(f'|{libraryDict[i][j][:22]}'.ljust(23),end='')
                    print('')
        elif selectMenu=='2':
            if len(libraryDict)==0:
                print('No Data Available!')
            else:
                showISBN=(input('Input the ISBN You Want To Show : '))
                if showISBN in libraryDict:
                    print('ISBN'.ljust(15),'|Title'.ljust(22),'|Author'.ljust(22),'|Status'.ljust(22),'|Loc/Return Date'.ljust(22),'|Borrower ID'.ljust(22))
                    print(f'{showISBN}'.ljust(16),end='')
                    for i in libraryDict[showISBN]:
                        print(f'|{libraryDict[showISBN][i][:22]}'.ljust(23),end='')
                else:
                    print('No Data Available!')
        elif selectMenu=='3':
            break

def mainAddBook():
    global libraryDict
    while True:
        print('\n'+' Add Book Information and Borrowing Status '.center(50,'-'),
        '\n1. Add Book Information and Borrowing Status',
        '\n2. Back')
        selectMenu=input('Select a Menu : ')
        if selectMenu=='1':
            addISBN=input('Please Input the ISBN of the Book you want to Add : ')
            
            if addISBN in libraryDict:
                print('Book is Already Exist in the Database')
            elif len(addISBN)==13 or len(addISBN)==10:
                addTitle=input('Please Input the Title of the Book : ')
                addAuthor=input('please Input the Author of the Book : ')
                addStatus=input('please Input the Status of the Book : ')
                addLocReturn=input('please Input the Location (if Available) or Return Date (if Unavailable) of the Book : ')
                if addStatus == 'Unavailable':
                    addBorrower=input('please Input the Borrower ID  : ')
                else:
                    addBorrower='-'
                while True:
                    print(' New Book Entry '.center(40,'_'),
                    f'\nTitle \t: {addTitle}',
                    f'\nAuthor \t: {addAuthor}',
                    f'\nISBN \t: {addISBN}',
                    f'\nStatus \t: {addStatus}',
                    f'\nLocation/Return Date \t: {addLocReturn}',
                    f'\nBorrower ID \t\t: {addBorrower}')
                    confirmAdd=input('Are you sure you want to add this book into the database? (Y/N) : ')
                    if confirmAdd=='Y':
                        libraryDict[addISBN]={'Title':addTitle,'Author':addAuthor,'Status':addStatus,'Return Date':addLocReturn,'Borrower ID':addBorrower}
                        print('Book Succesfully Added!')
                        break
                    if confirmAdd=='N':
                        break
                    else:
                        continue
            else:
                print('ISBN number must be in 13 digit or 10 digit number format') 
        elif selectMenu=='2':
            break
  
def mainUpdateBook():
    global libraryDict
    while True:
        print('\n'+' Change Book Information and Borrowing Status '.center(50,'-'),
        '\n1. Change Book Information and Borrowing Status',
        '\n2. Back')

        selectMenu=input('Select a Menu : ')

        if selectMenu=='1':
            updateISBN=input('Please Input the ISBN of the Book you want to Update : ')
            if updateISBN not in libraryDict:
                print(" Book Doesn't Exist in Database ".center(40,"!"))
            else:
                while True:
                    print(' Change Book Entry '.center(40,'_'),
                    f'\nISBN \t: {updateISBN}',
                    f'\nTitle \t: {libraryDict[updateISBN]["Title"]}',
                    f'\nAuthor \t: {libraryDict[updateISBN]["Author"]}',
                    f'\nStatus \t: {libraryDict[updateISBN]["Status"]}',                
                    f'\nReturn Date \t: {libraryDict[updateISBN]["Loc/Return Date"]}',
                    f'\nBorrower ID \t: {libraryDict[updateISBN]["Borrower ID"]}')
                    confirmUpdate=input('Are you sure you want to update this book information or status? (Y/N) : ')
                    if confirmUpdate=='Y':
                        oldTitle=libraryDict[updateISBN]['Title']
                        oldAuthor=libraryDict[updateISBN]['Author']
                        oldStatus=libraryDict[updateISBN]['Status']
                        oldReturn=libraryDict[updateISBN]['Loc/Return Date']
                        oldBorrower=libraryDict[updateISBN]['Borrower ID']
                        selectUpdate=input('Which Information You Wish To Update? (Title,Author,Status) : ')
                        if selectUpdate=='Title' or selectUpdate=='Author':
                            libraryDict[updateISBN][selectUpdate]=input(f'Please Input Your Update : ')
                        elif selectUpdate=='Status':
                            libraryDict[updateISBN]['Status']=input(f'Please Update Borrowing Status : ')          
                            libraryDict[updateISBN]['Loc/Return Date']=input(f'Please Update Return Date : ')     
                            libraryDict[updateISBN]['Borrower ID']=input(f'Please Update Borrower ID : ') 
                        while True:
                            print(' Updated Book Entry '.center(40,'_'),
                            f'\nISBN \t: {updateISBN}',
                            f'\nTitle \t: {libraryDict[updateISBN]["Title"]}',
                            f'\nAuthor \t: {libraryDict[updateISBN]["Author"]}',
                            f'\nStatus \t: {libraryDict[updateISBN]["Status"]}',                
                            f'\nReturn Date \t: {libraryDict[updateISBN]["Loc/Return Date"]}',
                            f'\nBorrower ID \t: {libraryDict[updateISBN]["Borrower ID"]}')
                            confirmUpdate2=input('Are you sure you want to save this changes? (Y/N) : ')  
                            if confirmUpdate2=='Y':
                                print('Book Successfully updated!')
                                break     
                            elif confirmUpdate2=='N':
                                libraryDict[updateISBN]['Title']=oldTitle
                                libraryDict[updateISBN]['Author']=oldAuthor
                                libraryDict[updateISBN]['Status']=oldStatus       
                                libraryDict[updateISBN]['Loc/Return Date']=oldReturn
                                libraryDict[updateISBN]['Borrower ID']=oldBorrower
                                break  
                        break                                                                     
                    elif confirmUpdate=='N':
                        break
            continue
        elif selectMenu=='2':
            break

def mainDeleteBook():
    global libraryDict
    while True:
        print('\n'+' Delete Book Information and Borrowing Status '.center(50,'-'),
        '\n1. Delete Book Information and Borrowing Status',
        '\n2. Back')
        selectMenu=input('Select a Menu : ')
        if selectMenu=='1':
            deleteISBN=input('Please Input the ISBN of the Book you want to Delete : ')
            if deleteISBN not in libraryDict:
                print(" Book Doesn't Exist in Database ".center(40,"!"))
            else:
                while True:
                    print(' Delete Book Entry '.center(40,'_'),
                    f'\nISBN \t: {deleteISBN}',
                    f'\nTitle \t: {libraryDict[deleteISBN]["Title"]}',
                    f'\nAuthor \t: {libraryDict[deleteISBN]["Author"]}',
                    f'\nStatus \t: {libraryDict[deleteISBN]["Status"]}',                
                    f'\nLoc/Return Date \t: {libraryDict[deleteISBN]["Loc/Return Date"]}',
                    f'\nBorrower ID \t\t: {libraryDict[deleteISBN]["Borrower ID"]}')
                    confirmUpdate=input('Are you sure you want to delete this book from database? (Y/N) : ')
                    if confirmUpdate=='Y':
                        del libraryDict[deleteISBN]
                        print('Book Successfully deleted from database!')
                        break                                                                     
                    elif confirmUpdate=='N':
                        break
                    else:
                        continue
            continue
        elif selectMenu=='2':
            break
        else:
            continue   

while True:
    print('\n'+' Welcome to Library Program - Book Information and Borrowing Status '.center(80,'|'),
    '\n\n'+' Program List '.center(50,'='),
    '\n1. Show Book Information and Borrowing Status',
    '\n2. Add Book Information',
    '\n3. Change Book Information and Borrowing Status',    
    '\n4. Delete Book Information and Borrowing Status',
    '\n5. Exit Program\n')
    selectProgram=str(input('Select a program : '))
    if selectProgram =='1':
        mainShowBook()
    elif selectProgram =='2':   
        mainAddBook()
    elif selectProgram =='3':
        mainUpdateBook()
    elif selectProgram =='4':
        mainDeleteBook()
    elif selectProgram=='5':
        break
    else:
        print('Invalid Input, Please Select a Program from the Menu !')
