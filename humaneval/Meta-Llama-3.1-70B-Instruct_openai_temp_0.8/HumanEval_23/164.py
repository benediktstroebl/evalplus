```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3

    :param string: Input string
    :return: Length of the input string
    """
    return len(string)


# Example usage:
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3

# Unit tests
import unittest

class TestStringLengthFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()
```