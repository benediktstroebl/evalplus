```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase (checked using `char.islower()`), it's converted to uppercase using `char.upper()`. If the character is uppercase, it's converted to lowercase using `char.lower()`. Finally, the modified characters are joined back into a string using `''.join(...)`.