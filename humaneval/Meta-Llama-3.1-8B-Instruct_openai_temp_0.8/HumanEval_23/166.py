```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): The input string.

    Returns:
    int: The length of the string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(""))  # Should print: 0
print(strlen("abc"))  # Should print: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is obtained using the built-in `len` function. The docstring for `strlen` provides a description of the function, its arguments, return value, and some examples of how to use it.