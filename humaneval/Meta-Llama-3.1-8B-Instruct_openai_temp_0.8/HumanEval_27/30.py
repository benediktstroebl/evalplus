```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that takes a string as input, iterates over each character in the string, and uses the `islower` method to check if the character is lowercase. If it is, the function converts it to uppercase using the `upper` method; otherwise, it converts it to lowercase using the `lower` method. The function then returns the resulting string. The script also includes documentation strings to provide context for the function and its usage.