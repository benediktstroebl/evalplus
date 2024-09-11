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
print(strlen("Hello, World!"))  # Expected output: 13
```

In this code, the `strlen` function returns the length of the input string using the built-in `len` function in Python. The test cases verify that the function behaves correctly for empty strings and strings of different lengths.