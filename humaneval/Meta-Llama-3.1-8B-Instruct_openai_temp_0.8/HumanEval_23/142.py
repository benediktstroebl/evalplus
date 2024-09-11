```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function to calculate the length, which makes the code concise and efficient. The docstring provides a description of the function, its arguments, and its return value, as well as some example use cases.