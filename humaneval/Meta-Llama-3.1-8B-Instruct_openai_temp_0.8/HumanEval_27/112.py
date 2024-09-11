```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

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
print(flip_case('AaBbCc'))  # Output: 'aAbBcC'
```

This script uses a generator expression to iterate over each character in the string. If the character is lowercase (`c.islower()` returns `True`), it's converted to uppercase (`c.upper()`); otherwise, it's converted to lowercase (`c.lower()`). The `join()` method is then used to combine the modified characters back into a string.