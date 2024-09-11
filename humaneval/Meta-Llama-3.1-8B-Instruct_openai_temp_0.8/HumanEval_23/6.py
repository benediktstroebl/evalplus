```markdown
### strlen Function

This script defines a function `strlen` to calculate the length of a given string.

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

### Testing the strlen Function

To test the `strlen` function, we can use the following code:

```python
import unittest

class TestStrlenFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_multiple_chars(self):
        self.assertEqual(strlen('hello world'), 11)

if __name__ == '__main__':
    unittest.main()
```

### Example Use Cases

You can use the `strlen` function in your own code like this:

```python
print(strlen('hello'))  # Output: 5
print(strlen('python'))  # Output: 6
```
```