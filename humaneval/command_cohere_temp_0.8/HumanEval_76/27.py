```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether `n` is an integer and if `x` is equal to `n` raised to the power of `x`, which is essentially the definition of a simple power. The type comparison ensures that the function handles invalid inputs gracefully, returning `False` for non-integer exponents. 

Here is a simple Python unit test framework to validate the function using the `unittest` module:
```python
import unittest

def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)

class TestSimplePower(unittest.TestCase):
    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

    def test_edge_cases(self):
        self.assertFalse(is_simple_power(0, 10))
        self.assertFalse(is_simple_power(-1, 2))
        self.assertTrue(is_simple_power(-2, -2)) 

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `test_is_simple_power` function tests various inputs to the `is_simple_power` function, checking if the function returns `True` for simple powers and `False` otherwise. The `test_edge_cases` function tests edge cases that are not intrinsic to the function but are still important to ensure proper functioning. The `unittest.main()` function runs the tests. 

To run the tests, you can simply run the script, and the `unittest` framework will run all the test cases and report the results. 

This framework is just one approach to testing; there are many other testing frameworks and methods available in Python for different needs. 

The script shows how to define tests for functions in Python using a simple testing framework, how to group related tests, and how to run them to verify functionality. 

You can adapt this code to test your own functions and develop more tests to increase code reliability.