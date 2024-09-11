```python
def flip_case(string: str) -> str:
    """ Flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case swapped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Expected output: 'hELLO'
print(flip_case('hELLO'))  # Expected output: 'Hello'
print(flip_case('aBc'))    # Expected output: 'AbC'
```

This Python script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and vice versa. The function uses a generator expression to iterate over each character in the string, checks if the character is lowercase using the `islower` method, and applies the `upper` or `lower` method accordingly. The resulting characters are then joined back into a string using the `join` method.