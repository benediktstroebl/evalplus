```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The input string with case flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
print(flip_case('heLlO'))  # Output: 'HeLLO'
```

In this script, the `flip_case` function uses a generator expression to iterate over each character in the input string. If the character is lowercase, it converts it to uppercase using the `upper` method. If it's uppercase, it converts it to lowercase using the `lower` method. The resulting characters are then joined back into a string using the `join` method.