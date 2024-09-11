```python
def get_positive(numbers: list):
    """
    Return a new list containing only the positive numbers from the input list.

    Args:
        numbers: A list of numbers.

    Returns:
        A list of positive numbers.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test the function
import unittest

class TestGetPositive(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
```

This script defines a function `get_positive` that takes a list of numbers and returns a new list containing only the positive numbers. It also includes a unit test using the `unittest` module to verify the function's behavior. The `if __name__ == '__main__':` block runs the unit test when the script is executed directly.