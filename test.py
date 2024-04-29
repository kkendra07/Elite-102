import unittest


#starter menu
def user_sel():
    input('What can we do for you? \n 1. Log in \n   2. Create Account \n 1-2:')
    if input == 1:
     log_in()
    elif input == 2:
     create_acc()

#starter functions 
def create_acc():
  print('ho')
  
def log_in():
  print('hi')

class Testuser_sel(unittest.TestCase):
    def test_login_val(self):
        self.assertEqual(user_sel())


if __name__ == '__main__':
    unittest.main()


    