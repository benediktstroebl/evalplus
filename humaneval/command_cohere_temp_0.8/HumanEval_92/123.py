```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

The function any_int takes three arguments, x, y, and z, and checks whether any of the three variables is equal to the sum of the other two variables. The function then checks whether the variables are integers, and if the above conditions are met, it returns True, otherwise, it returns False. 

Here is a self-contained Python script that includes corresponding tests for the function any_int:
```python
import unittest

def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False

class TestAnyInt(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(any_int(5, 2, 7))

    def test_example2(self):
        self.assertFalse(any_int(3, 2, 2))

    def test_example3(self):
        self.assertTrue(any_int(3, -2, 1))

    def test_example4(self):
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_negative_cases(self):
        self.assertFalse(any_int(-3, 2, -4))
        self.assertFalse(any_int(0, 0, 0))
        self.assertFalse(any_int(5, -6, 7))
        self.assertFalse(any_int(-4, -2, 2))

if __name__ == '__main__':
    unittest.main()
```

In this script, the `unittest` module is used to define four tests in the `TestAnyInt` class, which derive from `unittest.TestCase`. This class provides a variety of assertion methods, which can be used to create test cases. In each of these test methods, self.assertTrue is used to test if the any_int function returns True for a particular set of arguments; self.assertFalse is used to test if the any_int function returns False for a particular set of arguments. 

Finally, the `unittest.main()` function is called to run all the defined tests. 

To run the tests, you can run the script by typing python script_name.py into the CLI. 

To see all the assertions for each test, you can use the `--verbose` flag by typing `python -v script_name.py` into the CLI.