Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list `x` that contains only the positive elements of the input list `l`. 
The result is then returned as a new list of positive numbers. 
For example, if `l = [-1, 2, -4, 5, 6]`, then `get_positive(l)` will return `[2, 5, 6]`. 

Here's how you could test this function using the `unittest` module:
```python
import unittest

def get_positive(l):
    return [x for x in l if x > 0]

class TestGetPositive(unittest.TestCase):
    def test_get_positive_basic(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_get_positive_more_values(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()
```
This code will run the `unittest` module, which will run the two test methods defined in `TestGetPositive`. 
The `test_get_positive_basic` method tests the function with the basic example provided in the problem description. 
The `test_get_positive_more_values` method tests the function with a more complex example also from the problem description. 
Both tests will fail unless the function `get_positive` is correctly implemented to solve the problem. In this way, when you write `python test.py` in the terminal, the `unittest` module will run these tests and clearly report any failure, which will help you debug your code. 

Please note that for the tests to work, you have to save the `test.py` file in the same directory as the `get_positive.py` file and have the `unittest` module installed, which is usually the case in a Python distribution.  If you don't have it, you can install it with `pip install unittest` in the terminal.  In case you face any trouble, feel free to ask for assistance!