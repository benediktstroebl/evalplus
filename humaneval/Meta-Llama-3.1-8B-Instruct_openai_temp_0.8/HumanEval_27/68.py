```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string
    
    Returns:
    str: The string with case flipped
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
```

This script defines a function `flip_case` that uses Python's built-in string method `swapcase()` to flip the case of each character in the input string. The result is then returned as a string. The function is tested with the example provided in the docstring.