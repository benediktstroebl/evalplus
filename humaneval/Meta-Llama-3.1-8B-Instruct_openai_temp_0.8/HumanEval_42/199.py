```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [element + 1 for element in l]

# Test cases
import unittest

class TestIncrList(unittest.TestCase):
    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `incr_list` function, which uses a list comprehension to increment each element in the input list by 1. The function is then tested with two example use cases using the `unittest` module. If the function works correctly, the `unittest.main()` call will run the test cases and report any failures or errors.