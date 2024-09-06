```python
def is_simple_power(x, n):
    return type(x) == type(n)**int(n)**(x / n) and x == n**int(x / n)
```
This function checks if x is an integer, it returns true if n**int(x / n) == x, and false otherwise. If x is not an integer, the expression n**int(x / n) will throw an error and automatically return false. Also, to account for the possible floating-point errors, it is checking if the types of x and the result of n**int(x / n) are the same. 

Here is a test suite that verifies the correctness of the `is_simple_power` function.
```python
# Testing Suite for is_simple_power function
import unittest

def is_simple_power(x, n):
    return type(x) == type(n)**int(n)**(x / n) and x == n**int(x / n)

class TestIsSimplePower(unittest.TestCase):
    def test_is_simple_power_true(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertTrue(is_simple_power(100, 10))

    def test_is_simple_power_false(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

    def test_is_simple_power_non_int(self):
        self.assertFalse(is_simple_power(3.14, 2))
        self.assertFalse(is_simple_power(3.14, 3.14))

    def test_is_simple_power_different_types(self):
        self.assertFalse(is_simple_power("str", 2))
        self.assertFalse(is_simple_power([1, 2, 3], 3))
        self.assertFalse(is_simple_power({"a": 1, "b": 2}, 2))

if __name__ == '__main__':
    unittest.main()
```
In this test suite, the `test_is_simple_power_true` function verifies that the `is_simple_power` function returns True for inputs that should return true; the `test_is_simple_power_false` function verifies that the `is_simple_power` function returns False for inputs that should return false; the `test_is_simple_power_non_int` unit tests verify that the function recognizes non-integer inputs and returns False; and the `test_is_simple_power_different_types` unit tests verify that the function recognizes different types of inputs and returns False. 

Finally, the `unittest.main()` call runs the tests sequentially.