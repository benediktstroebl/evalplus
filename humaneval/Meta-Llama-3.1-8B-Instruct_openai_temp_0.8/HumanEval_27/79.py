```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip case.
    
    Returns:
        str: The string with flipped case.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
print(flip_case('aBc'))    # Output: 'ABc'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function uses a generator expression to iterate over each character in the string and a conditional expression to determine whether to convert it to uppercase or lowercase based on whether it is already uppercase or lowercase. The `join` method is then used to combine the characters back into a single string.