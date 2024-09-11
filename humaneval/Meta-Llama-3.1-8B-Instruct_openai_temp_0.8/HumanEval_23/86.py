```markdown
### strlen Function

A Python function to calculate the length of a given string.

```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
```

### Testing strlen Function

```python
import unittest

class TestStrlenFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()
```

### Usage

To use the `strlen` function, simply call it with a string as an argument:

```python
print(strlen('hello'))  # Output: 5
```