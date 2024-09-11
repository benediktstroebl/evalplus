```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase, it is uppercased; if it is uppercase, it is lowercased. The `join` method is then used to concatenate the characters back into a single string.