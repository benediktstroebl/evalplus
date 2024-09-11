```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list to be incremented.

    Returns:
        list: The incremented list.
    """
    return [x + 1 for x in l]

# Test cases
import unittest

class TestIncrList(unittest.TestCase):
    def test_increment_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `incr_list` function using list comprehension, which efficiently increments each element in the input list by 1. It also includes test cases to verify the function's correctness. When run, it will execute these tests and display their results.