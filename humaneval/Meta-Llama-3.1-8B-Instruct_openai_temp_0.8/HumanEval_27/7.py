```python
def flip_case(string: str) -> str:
    """ Flip the case of all characters in a given string.

    Args:
        string (str): The input string to flip the case of.

    Returns:
        str: The input string with all characters flipped in case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)
```

This function uses Python's built-in `lower()` and `upper()` string methods to flip the case of each character in the input string. The `isupper()` method checks if a character is uppercase, and `join()` concatenates the modified characters back into a single string. The function is written in a clear and concise way, following standard professional guidelines for docstrings, function signature, and comments.