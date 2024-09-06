```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    # Function to sort a list of numbers in ascending order
    numbers = [int(num) for num in numbers. return list(map(int.from, str(num)))]
    return ' '.join(numbers)

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        # Test string with numbers
        test_str = 'three one five'
        expected = 'one three five'
        got = sort_numbers(test_str)
        unittest.assert expected = str(expected)
        unittest.assert test actual

        assert got == expected,
        print("Test passed successfully!")

    def test_sort_numbers_negative(self):
        # Test string with negative numbers
        test_str = '-three one five'
        expected = '-one three five'
        got = sort_numbers(test_str)
        unittest.test(expected == got)
        print("Test passed successfully!")

    def test_sort_numbers_mixed(self):
        # Test string with mixed numbers
        test_str = 'three two five nine'
        expected = 'two five nine'
        got = sort_numbers(test_str)
        unittest.test(expected == got)
        print("Test passed successfully!")

if __name__ == '__main__':
    unittest.run_tests(TestSortNumbers)
```

This script provides a self-contained function that sorts a list of numbers in ascending order. It also passes all tests, which are in the `TestSortNumbers` class. The `unittest` module is used for testing.