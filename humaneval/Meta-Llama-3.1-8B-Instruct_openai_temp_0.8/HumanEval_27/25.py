```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

This script defines a function `flip_case` that takes a string as an input and returns a new string where all lowercase characters are converted to uppercase and vice versa. The function uses a generator expression inside the `join` method to iterate over each character in the string, flip its case, and concatenate the result.