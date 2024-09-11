```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is obtained using the built-in `len` function, which is what this script uses. The docstring provides a description of the function, its argument and return value, and some examples of how it can be used.