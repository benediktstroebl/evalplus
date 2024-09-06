Here's a Python script with a self-contained function `generate_even_digits()` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    if a % 2 or b % 2:
        return []

    max_digit = max(a, b)
    even_digits = [str(i) for i in range(a, b + 1) if i % 2 == 0]
    return even_digits
```

This function handles cases where either `a` or `b` (or both) are odd and returns an empty list as the result. It also uses a list comprehension to efficiently find the even digits between the two numbers.

You can use the module `unittest` to create and run tests:
```python
import unittest

class TestEvenDigits(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(generate_even_digits(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_even_digits(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_even_digits(10, 14), [])

    def test_with_odd_numbers(self):
        self.assertEqual(generate_even_digits(5, 7), [6])
        self.assertEqual(generate_even_digits(1, 11), [])

    def test_max_digit(self):
        self.assertEqual(max(generate_even_digits(100, 200)), 98)

if __name__ == '__main__':
    unittest.main()
```

We create three test functions to cover different scenarios: `test_basic`, `test_with_odd_numbers`, and `test_max_digit`. The `unittest.main()` call runs all the tests when you run the script.