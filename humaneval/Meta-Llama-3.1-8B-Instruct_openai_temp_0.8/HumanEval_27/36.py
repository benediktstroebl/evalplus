```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to be modified.

    Returns:
    str: The modified string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

This script defines a function `flip_case` that takes a string as input and returns the modified string with lowercase characters converted to uppercase and vice versa. The `islower()` method checks if a character is lowercase and the `upper()` and `lower()` methods are used to convert characters accordingly. The result is then joined back into a string using `''.join()`.