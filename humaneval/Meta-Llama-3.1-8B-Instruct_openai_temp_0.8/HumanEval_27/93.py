**Flipping Case in a String**
================================

This script defines a function `flip_case` that takes a string as input and returns a new string with lowercase characters flipped to uppercase and vice versa.

```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])
```

**Testing the Function**
------------------------

```python
import unittest

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('hello'), 'HELLO')
        self.assertEqual(flip_case('HELLO'), 'hELLO')
        self.assertEqual(flip_case(''), '')
        self.assertEqual(flip_case('123'), '123')

if __name__ == '__main__':
    unittest.main()
```

To run the tests, save both scripts in the same directory and execute the testing script. The tests will ensure that the `flip_case` function behaves as expected.