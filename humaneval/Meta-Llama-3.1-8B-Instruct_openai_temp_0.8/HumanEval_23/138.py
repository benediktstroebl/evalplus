### strlen Function Implementation
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
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. The function includes a docstring that provides a description, explains the function's parameters and return value, and includes examples of its usage.