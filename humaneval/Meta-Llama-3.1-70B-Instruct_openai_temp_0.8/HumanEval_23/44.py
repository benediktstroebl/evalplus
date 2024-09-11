```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


# Test cases
import unittest

class TestStringLengthFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()
```

This script defines a `strlen` function that uses Python's built-in `len` function to calculate the length of a given string. It includes a docstring with usage examples. The script also includes test cases using Python's `unittest` module to verify the function's behavior.