```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
    string (str): The input string

    Returns:
    int: The length of the string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Testing the function
print(strlen(""))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len()` function in Python is used to get the length of a string. The docstring explains what the function does, what arguments it takes, and what it returns. The examples show how to use the function and what output to expect.