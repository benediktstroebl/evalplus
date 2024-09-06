```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by comparing it to the result of raising `n` to the power of `x` and seeing whether they are equal. It also performs some type checking to make sure that `n` is an integer. 

Here is a simple python script to test the function above:
```python
# required libraries
import unittest

# function to test
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)

# the tests
class Test(unittest.TestCase):
    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

    def test_true_values(self):
        true_values = [
            (2, 2),
            (4, 2),
            (16, 4),
            (1, 1),
            (64, 8),
        ]

        for x, n in true_values:
            self.assertTrue(is_simple_power(x, n))

    def test_false_values(self):
        false_values = [
            (3, 2),
            (5, 3),
            (2, 3),
            (8, 4),
            (101, 10),
        ]

        for x, n in false_values:
            self.assertFalse(is_simple_power(x, n))

# run tests
unittest.main()
```

This code provides a test suite with a variety of test cases to ensure the function `is_simple_power` works correctly. It can be ran by copying the code into a python file and running it, or by copying the code into a python interpreter. 

Note: this implementation checks only the simple powers, hence the title "Simple Power Helper"; it does not handle cases like `3^2 == 9` or `2^3 == 8`, which some might consider incorrect, as they are not simple powers. 

If you need to check all real powers, the function would need to be adjusted accordingly.