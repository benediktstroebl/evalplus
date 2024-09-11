```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Testing the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length. We then use the built-in `len` function to calculate the length of the string. The docstring explains the purpose of the function, and the test cases demonstrate its usage.