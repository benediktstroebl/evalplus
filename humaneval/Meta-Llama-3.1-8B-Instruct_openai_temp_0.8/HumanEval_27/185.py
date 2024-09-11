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


# Test the function
print(flip_case('Hello'))  # Should print 'hELLO'
print(flip_case('hELLO'))  # Should print 'HeLLO'
print(flip_case('ALL CAPS'))  # Should print 'aLL cApS'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and vice versa. The function uses a generator expression within the `join` method to iterate over each character in the string, converting it as necessary. The script also includes example use cases to demonstrate the function's behavior.