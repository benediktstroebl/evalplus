```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3

# You can also use the built-in unittest framework for more comprehensive testing
import unittest

class TestStringLenFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_long_string(self):
        self.assertEqual(strlen('abcdefghijklmnopqrstuvwxyz'), 26)

if __name__ == '__main__':
    unittest.main()

```

In this code:

1. We define a function `strlen` that takes a string as input and returns its length using the built-in `len` function.

2. We include a docstring that provides a description of what the function does, explains the input and output parameters, and provides examples of how to use the function.

3. We include test cases using both the `assert` statement and the `unittest` framework to verify that the function behaves correctly for different inputs.