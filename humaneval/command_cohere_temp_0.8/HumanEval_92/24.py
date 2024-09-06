```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return a or b or c
```

This function checks if any combination of the three variables adds up to the other variable. It works with the properties of the integers and does not require any floating point or irrational numbers. 

Here is a self-contained Python script that uses the function above to check if any of the three numbers are equal to the sum of the other two:
```python
import unittest
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return a or b or c

class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
    def test_any_int_multiple_args(self):
        self.assertTrue(any_int(1, 2, 3, 4, 5))
        self.assertFalse(any_int(1, 2, 3, 4, 5, 6))
    def test_any_int_empty(self):
        self.assertFalse(any_int())
    def test_any_int_invalid_args(self):
        with self.assertRaises(TypeError):
            any_int(1, 2, 3.5)
        with self.assertRaises(TypeError):
            any_int(1, 2, 3, 4, 5, 6.5)
if __name__ == '__main__':
    unittest.main()
```

This script creates a test class with unit tests to check if the function `any_int` works correctly with different inputs. Each test checks a different condition and passes or fails accordingly. 
The `unittest.main()` function is required to run the tests. 

To run the script, save it in a Python file (e.g., `test_any_int.py`) and execute it with the Python interpreter:
```
python test_any_int.py
``` 
The interpreter will run the tests and provide you with a summary of the results, including the number of tests passed, failed, or raised errors. 

This way, you can validate the correctness of the function and ensure that it adheres to the problem statement.