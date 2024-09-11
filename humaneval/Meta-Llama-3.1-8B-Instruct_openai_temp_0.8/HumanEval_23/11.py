```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This script defines the `strlen` function, which takes a string as input and returns its length. It uses the built-in `len` function to calculate the string length. The test cases at the end verify the function's behavior for empty strings and non-empty strings.