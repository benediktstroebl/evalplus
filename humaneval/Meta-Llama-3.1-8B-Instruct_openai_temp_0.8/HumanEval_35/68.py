```python
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    return max(l)

# Test cases
import unittest

class TestMaxElementFunction(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
```

This script does the following:

1. Defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list.
2. Uses the built-in `max` function in Python to find the maximum element in the list.
3. Tests the `max_element` function using the `unittest` framework to ensure it works correctly for different inputs.
4. Runs the tests when the script is executed directly.