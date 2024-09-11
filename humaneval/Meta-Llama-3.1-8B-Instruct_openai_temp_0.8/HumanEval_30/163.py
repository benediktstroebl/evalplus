```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers: A list of numbers.

    Returns:
        A list of positive numbers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test the function
from unittest import TestCase

class TestGetPositive(TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == "__main__":
    import unittest
    unittest.main(argv=[sys.argv[0]])
```

This script defines the `get_positive` function using a list comprehension to filter out non-positive numbers, and includes unit tests to ensure the function behaves as expected.