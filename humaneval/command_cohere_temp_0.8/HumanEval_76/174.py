```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating the condition `n ** int(x == n ** x)`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function also checks that the type of `n` is integer, which is part of the problem statement's requirements. 

Here is a simple `unittest` test suite to verify the functionality of the function: 
```python
import unittest

def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)

class TestIsSimplePower(unittest.TestCase):
    def test_is_simple_power_true(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        # Test case with large exponent
        self.assertTrue(is_simple_power(1337, 1337))

    def test_is_simple_power_false(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        # Test case with non-integer base
        self.assertFalse(is_simple_power(2, 1.5))

    def test_is_simple_power_edge_cases(self):
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(4, 2))
        self.assertFalse(is_simple_power(5, 2))

if __name__ == '__main__':
    unittest.main()
``` 

The `unittest` test suite covers various scenarios, including edge cases, to ensure the function `is_simple_power` behaves as expected. 

This code will run the tests automatically whenever the script is executed. It will also highlight which specific tests fail, making it easier to debug. 

Ensure the requirements (e.g., `unittest`) are installed in your Python environment to run the tests successfully.  You can do it in Python scripts or in an IDE alike.