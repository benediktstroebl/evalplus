```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('Python'))  # Output: 'pYTHON'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with the case of each character flipped. The function uses a list comprehension to iterate over each character in the string. If the character is lowercase, it is converted to uppercase using the `upper` method; otherwise, it is converted to lowercase using the `lower` method. The resulting characters are then joined back together into a string using the `join` method.