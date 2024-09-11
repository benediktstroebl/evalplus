```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with cases flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```

This script uses a generator expression to iterate over each character in the string. If the character is lowercase, it is converted to uppercase using the `upper()` method; otherwise, it is converted to lowercase using the `lower()` method. The `join()` function is then used to combine the characters back into a single string.