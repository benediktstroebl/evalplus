```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): Input string.

    Returns:
        int: Length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases using Python's built-in unittest module
import unittest

class TestStringLengthFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('a b c'), 5)

if __name__ == '__main__':
    unittest.main()
```

This script defines the `strlen` function to calculate the length of a given string using the built-in `len` function. It includes a docstring for documentation and test cases using Python's `unittest` module to ensure the function behaves as expected.