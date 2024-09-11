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
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is given by the built-in `len` function, which is why we use it here. The docstring includes a description of the function, its parameters, return value, and some examples of how it can be used.