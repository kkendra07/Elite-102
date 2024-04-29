import unittest


#starter menu
#def user_sel():
#    input('What can we do for you? \n 1. Log in \n   2. Create Account \n 1-2:')
#    if input == 1:
#     log_in()
#    elif input == 2:
#     create_acc()

#starter functions 
#def create_acc():
#  print('ho')
  
#def log_in():
 # print('hi')

#class Testuser_sel(unittest.TestCase):
  #  def test_login_val(self):
 #       self.assertEqual(user_sel())


#if __name__ == '__main__':
#    unittest.main()

#check function

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'elite102', password = 'n0tK0727!')

cursor = connection.cursor() 

def menu():
 print("menu")

global account_number
global pin
account_number = 409386429
pin = 9090

def check():
  testQuery = ('SELECT number FROM user_info')
  cursor.execute(testQuery)
  
  for item in cursor:
    if item == account_number:
        testQuery = ('SELECT row FROM user_info')
        cursor.execute(testQuery)

        if item in cursor == account_pin:
          menu()




#test
class Testcheck(unittest.TestCase):
    def test_ifcheck(self):
        self.assertTrue(check())


if __name__ == '__main__':
    unittest.main()
    
    
cursor.close()