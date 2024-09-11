```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3

# Test cases using the unittest framework
import unittest

class TestStrlenFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_single_character_string(self):
        self.assertEqual(strlen('a'), 1)

if __name__ == '__main__':
    unittest.main()
```

This Python script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The script also includes example usage and test cases using the `unittest` framework to verify the correctness of the `strlen` function.