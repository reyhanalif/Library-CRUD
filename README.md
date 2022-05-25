# Library-CRUD - Book management for Library created in Python

Hello everyone! This is a simple CRUD program created in Python about Book Management for Library. This program intended to demonstrate basic python computation such as conditiononal statement, looping, data collection type, and function. I made this program as a project for Python Introduction on Purwadhika Data Science Program. Making a CRUD program is great way to learn and implement all of the basics in programming. In order to complete or add some feature to our program, it also triggers our curiousity to seek another function on a programming language.

Let's take a look at this program main function.

## 1. Show Book Information and Borrowing Status
This function serves to show the book information and also the current borrowing status of the book in the library. 

There are 2 option in this function: 
1. Show [All] Book Information and Borrowing Status 

    If you want to display all of the book information and status in the library

2. Show [Specific] Book Information and Borrowing Status 

    if you want to display certain book information and status in the library by inputing an ISBN 

## 2. Add Book Information and Borrowing Status
This function serves to add book information and borrowing status into our database. 

This function requires you to input information below:
1. Title 
2. Author
3. ISBN
4. Status 
5. Location/Return Date 
6. Borrower ID 

## 3. Change Book Information and Borrowing Status
This function serves to change book information and borrowing status in our database.

This is the function you'd want to use to manage In and Out of your books by updating the book status. 

**When a book is borrowed by a member,** 
1. Input the keyword 'Status' when the program prompts 'Which Information You Wish To Update?'
2. Update the Status into 'Unavailable'
3. Input the Return Date of the book
4. Input the ID of the borrower
5. Confirm Changes


**When a book is returned,**
1. Input the keyword 'Status' when the program prompts 'Which Information You Wish To Update?'
2. Update the Status into 'Available'
3. Input the Shelves Number (Location) where the book stored
4. Input the Borrower ID with keyword '-'
5. Confirm Changes

**In Case there is an update to book information,** 
1. Input the keyword 'Title' or 'Author' when the program prompts 'Which Information You Wish To Update?'
2. Input your update 
3. Confirm Changes

## 4. Delete Book Information and Borrowing Status
This is the function if you want to delete a book from your database

Input ISBN of the book you wish to delele and confirm change to proceed

## Foreword
That's it for the first project I made as a student in Purwadhika, feel free to catch me up if you have any feedback or suggestion, I'd really appreciate to hear your toughts!

See you in the next project.
