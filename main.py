#IMPORT
import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'elite102', password = 'n0tK0727!')
cursor = connection.cursor()  



import tkinter as tk
from tkinter import ttk

root = tk.Tk()


#APP CODE 
message = tk.Label(root, text="Welcome to K Banks!")
message.pack()
root.geometry('600x400+50+50')
root.resizable(True, True) 
root.attributes('-topmost', 1) 
#root.iconbitmap('bank-vector-icon.ico')

#main menus 
def user_sel():
    root.title('K Banks Sign in')

    login_button = ttk.Button(root, text="Log in", command=log_in)
    login_button.pack(ipadx=10, ipady=10, expand=True)

    signin_button = ttk.Button(root, text="Create Account", command=create_acc)
    signin_button.pack(ipadx=10, ipady=10, expand=True)

    input('What can we do for you? \n 1. Log in \n   2. Create Account \n 1-2:')
    if input == '1':
     log_in()
    elif input == '2':
     create_acc()




def menu():
  root.title('Main menu')
  input('Good Evening! \n What would you like to do? \n 1. Make a deposit \n 2. Make a withdraw \n 3. Check Balance \n 4. Manage account \n 1-4:')
  if input == '1':
    deposit()
  elif input == '2':
    withdraw()
  elif input == '3':
    balance()
  elif input == '4':
    acc_manage()




#main functions
def create_acc():
  account_number = int(input("Welcome! Lets get started by creating a 9 digit accont number"))
  #if account_number == number in user_info:
    #print('Account already exists, please sign in or try again.')
    #user_sel() 
  count_digit(input)
  if count_digit == 9: 
   addData = ('INSERT INTO user_info (number) VALUES', (account_number))
   cursor.execute(addData)


  print("Great! Please enter your Name and a 4 digit pin to access your account.")
  user_name = input("Name:")
  count_digit(input)

  addData = ('INSERT INTO user_info (name) VALUES', (user_name))                          
  cursor.execute(addData)
  
  pin_number = int(input('Pin Number:'))
  if count_digit == 4:
  
   addData = ('INSERT INTO user_info (pin) VALUES', (pin_number))                               
   cursor.execute(addData)

   print("You're all set! \n Please return to login.")
   user_sel()
  else:
   print("Sorry! Could'nt understand!")
   create_acc()


  
def log_in():
  root.title('K banks log in')

  ttk.Label(root, text='Hello! Please log in.').pack()

  testQuery = ('SELECT number FROM user_info')
  cursor.execute(testQuery)

  accnum_label = ttk.Label(root, text="Account number:")
  accnum_label.pack(fill='x', expand=True)

  accnum_entry = ttk.Entry(root, textvariable=account_number)
  accnum_entry.pack(fill='x', expand=True)
  accnum_entry.focus()

  account_number = int(input("Please enter your 9 digit account number:"))
 
  for item in cursor:
    if item == input:
        testQuery = ('SELECT row FROM user_info')
        cursor.execute(testQuery)

        pin_label = ttk.label(root, text="Pin:")
        pin_label.pack(fill='x', expand=True)

        pin_entry = ttk.entry(root, textvariable=account_pin)
        pin_entry.pack(fill='x', expand=True)

        account_pin = int(input("Please enter your 4 digit pin:"))

        if item in cursor == input:
          menu()
      


    
  
def deposit():
  amount_deposit = int(input("How much would you like to deposit?"))
  
  new_balance = f'{amount_deposit} + balance in user_info' 

  addData = ('REPLACE INTO user_info(balance) VALUES ', (new_balance))                     
  cursor.execute(addData)

  input("Balance updated! \n Would you like to make another deposit? \n yes/no:")
  if input == 'yes':
    deposit()
  elif input == 'no':
    menu()
  



def withdraw():
  amount_withdrawn = input("How much would you like to withdraw?")

  new_balance = f'balance in user_info - {amount_withdrawn}' 

  addData = ("REPLACE INTO user_info(balance) VALUES", (new_balance))                             
  cursor.execute(addData)

  input("Balance updated! \n Would you like to make another withdraw? \n yes/no:")
  if input == 'yes':
    withdraw()
  elif input == 'no':
    menu()

  #elif amount_withdraen is more than balance in table:
    #print('Imsuficient funds, please make a deposit or try again later')
    #menu()

  
def balance():
  print("Your current balance is")

  testQuery = ('SELECT balance FROM user_info')
  cursor.execute(testQuery)
  

  



def acc_manage(): 
  input('What would you like to do? \n 1. Chance name \n 2. Change pin \n 3.Delete account')
  if input == '1':
   new_name = input('Please enter your changed name:')
   
   addData = ('REPLACE INTO user_info(name) VALUES', (new_name))                                   
   cursor.execute(addData)

   ex()

  elif input == '2':
    new_pin = input('Please enter your changed pin:')
    
    addData = ('REPLACE INTO user_info(pin) VALUES', (new_pin))                               
    cursor.execute(addData)

    ex()

  elif input == '3':
    input("Are you sure you'd like to delete your account? \n yes/no:")
    if input == 'yes':
      
      removeData = ('DELETE row FROM user_info')
      cursor.execute(removeData)

    elif input == 'no':
      acc_manage()
  else:
   print("Sorry! Couldn't understand.")
   acc_manage()
  
  



#SIDE FUNCTION
def ex():
  input("You're all set! Anyhting else you'd like to do here? \n yes/no:")
  if input == 'yes':
     acc_manage()
  elif input == 'no':
     menu()



def count_digit(num):
    if (num//10 == 0):
        return 1
    else:
        return 1 + count_digit(num // 10)

 

#CODE FOR TKINTER
#main menus TKINTER

#login_button = ttk.Button(root, text="Log in", command=log_in)
#login_button.pack(ipadx=10, ipady=10, expand=True)

#signin_button = ttk.Button(root, text="Create Account", command=create_acc)
#signin_button.pack(ipadx=10, ipady=10, expand=True)

#mainmenu_button = ttk.Button(root, text='Exit', command=menu)
#mainmenu_button.pack(ipadx=5, ipady=5, expand=True)



#IMPORT CLOSE AND FUNCTION CALL
connection.commit()

cursor.close()

connection.close()

user_sel()

root.mainloop()

