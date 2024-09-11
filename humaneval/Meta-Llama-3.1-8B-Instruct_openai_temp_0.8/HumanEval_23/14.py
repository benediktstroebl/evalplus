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
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. The docstring explains the purpose of the function, its arguments, return value, and includes example use cases.