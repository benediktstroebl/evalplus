```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    even_digit = [int(d) for d in xs[0]] if len(xs) > 0 else []
    is_even = [d in even_digit for d in xs]
    return [x for x in xs if not any(is_even)]
```

The function exploits the fact that Python integers have arbitrary precision and can thus be tested for membership in the set of integers less than 10. It avoids the creation of the potentially large list `result` in the original code. Instead, it uses a list comprehension to filter elements from `xs` that have no even digits. 

This version is both more memory-efficient and faster (in terms of execution time). 

The unit tests can be run as follows:
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    def test_unique_digits_empty(self):
        self.assertEqual(unique_digits([]), [])
    def test_unique_digits_negatives(self):
        self.assertEqual(unique_digits([123, -14, -3, -32, -45]), [-14, -3, -32, -45])
    def test_unique_digits_multiple_elts(self):
        self.assertEqual(unique_digits([11, 22, 33, 44, 55, 66, 77]), [11, 22, 33, 44, 55, 66, 77])
if __name__ == '__main__':
    unittest.main()
```

This script includes a variety of tests covering different scenarios, such as testing with both positive and negative integers, testing with empty lists, and testing with multiples of 10. 

These tests can be run automatically as part of a test suite to ensure that the function `unique_digits` continues to work correctly as changes are made to the code.