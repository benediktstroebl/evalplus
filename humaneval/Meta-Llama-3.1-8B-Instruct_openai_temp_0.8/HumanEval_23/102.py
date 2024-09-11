```python
def strlen(string: str) -> int:
    """Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. It also includes a docstring that describes the function's behavior, parameters, return value, and provides examples of usage. If the input is not a string, the function raises a `TypeError`.