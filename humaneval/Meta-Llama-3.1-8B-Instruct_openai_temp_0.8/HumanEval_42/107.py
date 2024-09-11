```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test cases
import unittest

class TestIncrList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
    def test_mixed(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `incr_list` function, which returns a new list where each element is incremented by 1. It uses a list comprehension for a concise solution.

The test cases are written using the `unittest` framework, which is part of the Python standard library. The `unittest.main()` call runs the tests. If all tests pass, you won't see any output. If a test fails, you'll see an error message.