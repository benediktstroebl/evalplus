### Increment List Function
```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of integers.

    Returns:
        list: List with elements incremented by 1.
    """
    return [i + 1 for i in l]

# Test cases
import unittest

class TestIncrList(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_realistic_list(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `incr_list` function which increments each element in the input list by 1. It then includes test cases to verify its correctness. You can run the script to see the test cases pass.