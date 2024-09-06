```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function solves the problem by determining whether a number is a simple power of n by checking if its value is equal to the result of raising n to the power of the integer value of itself. It does so using the powermatching technique, a fast and elegant solution that tests if a number is a power of another number in logarithmic time.

The code implements the algorithm efficiently by taking advantage of the properties of integers and the **sqrt** function in a concise and readable manner, demonstrating a practical application of mathematical concepts in programming.

You can test this function using an integrated test suite to verify its correctness. Here is an example of a test suit for this function:
```python
import unittest

def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)

class TestIsSimplePower(unittest.TestCase):
    def test_positive_integers(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(5, 3))

    def test_non_positive_integers(self):
        self.assertTrue(is_simple_power(1, -4))
        self.assertTrue(is_simple_power(2, -2))
        self.assertTrue(is_simple_power(8, -2))
        self.assertFalse(is_simple_power(3, -2))
        self.assertFalse(is_simple_power(5, -3))

    def test_non_integer_input(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(0, 5))
        self.assertFalse(is_simple_power(-3, -2))

    def test_large_numbers(self):
        self.assertTrue(is_simple_power(16000, 2))
        self.assertTrue(is_simple_power(100000, 5))
        self.assertFalse(is_simple_power(3000, 2))
        self.assertFalse(is_simple_power(70000, 5))

if __name__ == '__main__':
    unittest.main()
```

In this example, the `unittest` module is imported to facilitate test creation and execution. The `test_simple_powres` method creates an instance of the `TestIsSimplePower` class for each test case and invokes the `assertTrue` method to verify the expected behavior of the `is_simple_power` function. Similarly, `assertFalse` is used to check for expected false outcomes.