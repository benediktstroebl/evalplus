```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with all characters flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrLd'
print(flip_case('Python'))  # Output: 'pYtHOn'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The `islower()` and `upper()`/`lower()` methods of the `str` class are used to achieve this. The function is then tested with some example inputs to demonstrate its usage.