```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function checks if a number `x` is a simple power of `n` by comparing `x` to the result of raising `n` to the power of `int(n ** 0.5)`, which is the largest integer less than or equal to `n ** 0.5`. The function returns `True` if `x` is a simple power of `n`, and `False` otherwise.

Here is a simple `unittest` test suite example to verify the functionality of the `is_simple_power()` function:
```python
import unittest

def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)

class TestIsSimplePower(unittest.TestCase):
    def test_is_simple_power_1(self):
        self.assertTrue(is_simple_power(1, 4))

    def test_is_simple_power_2(self):
        self.assertTrue(is_simple_power(2, 2))

    def test_is_simple_power_3(self):
        self.assertTrue(is_simple_power(8, 2))

    def test_is_simple_power_4(self):
        self.assertFalse(is_simple_power(3, 2))

    def test_is_simple_power_5(self):
        self.assertFalse(is_simple_power(3, 1))

    def test_is_simple_power_6(self):
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()
```

In this example, the `unittest` module is imported, and a test class `TestIsSimplePower` is defined, inheriting from `unittest.TestCase`. Each test case is a method within this class, starting with the prefix `test_`. The `unittest.main()` function is necessary to discover and run the test cases. 

To run the tests, you can save the tests and the function definition in separate files (e.g., `test_is_simple_power.py` and `is_simple_power.py`), and then execute the test file using the command `python test_is_simple_power.py` in your terminal. 

This will run all the test cases and provide you with a detailed report on whether the function is correctly determining simple powers. You can also put all these into a single file if you like.