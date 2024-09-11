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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of an object, including strings. The docstring at the top of the function provides documentation and test cases. The test cases at the bottom of the script are used to verify that the function is working correctly.