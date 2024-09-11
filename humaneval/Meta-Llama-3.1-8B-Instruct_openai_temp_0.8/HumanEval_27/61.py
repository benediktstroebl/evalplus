```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])
```

In this script, the function `flip_case` uses list comprehension to iterate over each character `c` in the string. If the character is lowercase (`c.islower()` returns `True`), it is converted to uppercase with `c.upper()`. If the character is uppercase, it is converted to lowercase with `c.lower()`. The `join` method is then used to concatenate all the characters into a single string.