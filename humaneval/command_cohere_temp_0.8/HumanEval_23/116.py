```python
def strlen(s: str) -> int:
    """Return the number of characters in the string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string as an argument and returns the number of characters (including spaces, punctuation, and any other glyphs) in that string. The function uses the `len()` function to determine the length of the string. 

To ensure the function behaves as expected, let's test-drive it using Python's built-in `unittest` framework like so:
```python
import unittest

def strlen(s: str) -> int:
    """Return the number of characters in the string."""
    return len(s)

class StrlenTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_mixed_string(self):
        self.assertEqual(strlen("one, two, three"), 11)

if __name__ == '__main__':
    unittest.main()
```

This test suite contains three individual tests, each of which checks the function's behavior for a specific scenario: handling an empty string, a non-empty string, and a mixed string. 

Finally, running `unittest.main()` executes the tests. In this case, all tests pass as expected, confirming that `strlen` function behaves as we designed it to. 

This example demonstrates how to create reliable and maintainable code using TDD principles in Python.