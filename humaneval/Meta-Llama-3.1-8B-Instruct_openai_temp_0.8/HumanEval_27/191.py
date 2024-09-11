```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with lowercase and uppercase characters flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)

# Test the function
print(flip_case('Hello'))
```

This script defines a function `flip_case` that takes a string as input and returns the string with lowercase characters changed to uppercase and vice versa. The function uses a generator expression to iterate over each character in the string, checks if the character is uppercase using the `isupper` method, and applies the `lower` or `upper` method accordingly. The resulting characters are then joined back together into a string using the `join` method.