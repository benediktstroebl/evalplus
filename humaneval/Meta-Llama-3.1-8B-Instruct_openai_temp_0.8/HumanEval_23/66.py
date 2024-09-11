```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): Input string.

    Returns:
    int: Length of the input string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function is used to calculate the length of the string. The docstring provides a description of the function, its arguments, and its return value. It also includes example use cases to demonstrate how to call the function.