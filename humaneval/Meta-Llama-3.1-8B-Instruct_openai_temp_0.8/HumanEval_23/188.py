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

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string. The docstring includes doctest examples to verify the function's behavior. The test cases at the end print the expected output when calling the `strlen` function with an empty string and a string with three characters.