```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is obtained using the built-in `len` function. The script then tests the `strlen` function with some example inputs.