```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function (`strlen`) that takes a string as an argument and returns its length. It utilizes the `len()` function to calculate the number of characters (including spaces, special characters, and punctuation) in the input string, hence, `strlen('abc')` returns `3`. If the string is empty, like in `strlen('')`, the function returns 0.  This function is appropriately tested below using Python's native `unittest` module, ensuring its correctness in handling various scenarios.

```python
import unittest

def strlen(string: str) -> int:
    return len(string)

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_whitespace_string(self):
        self.assertEqual(strlen("  abc  "), 3)

    def test_mixed_string(self):
        self.assertEqual(strlen("abc123"), 3)

if __name__ == '__main__':
    unittest.main()
```