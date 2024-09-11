```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)
```

In this script, we use a generator expression to iterate over each character in the input string. If the character is lowercase (checked using `char.islower()`), we convert it to uppercase using `char.upper()`. Otherwise, we leave the character as it is (i.e., convert it to lowercase). The resulting characters are then joined together into a single string using `''.join(...)`.