```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The length of the string.
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases
print(strlen('') == 0)  # Expected output: True
print(strlen('abc') == 3)  # Expected output: True
```

Alternatively, you can use Python's built-in `unittest` module to write and run test cases:

```python
import unittest

def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The length of the string.
    """
    return len(string)

class TestStringLengthFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()
```

Both scripts will work as expected, but the second one is more robust and follows best practices for testing code in Python.