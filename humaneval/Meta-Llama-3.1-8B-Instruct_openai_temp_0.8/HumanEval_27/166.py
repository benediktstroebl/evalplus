```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('World'))  # Output: 'wORLD'
print(flip_case('Python'))  # Output: 'pYTHON'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function uses a generator expression to iterate over each character in the string, checks whether the character is lowercase using the `islower` method, and converts it to the opposite case using the `upper` and `lower` methods. The results are then joined back into a string using the `join` method.