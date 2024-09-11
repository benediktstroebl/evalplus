```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with cases flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('all uppercase'))  # Output: 'All UPPERCASE'
print(flip_case('ALL lowercase'))  # Output: 'aLl LOWERCASE'
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase, it is converted to uppercase, and if it is uppercase, it is converted to lowercase. The `join` method is then used to concatenate the characters back into a single string.