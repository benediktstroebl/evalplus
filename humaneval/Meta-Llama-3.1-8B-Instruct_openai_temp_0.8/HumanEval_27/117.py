```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: The string with case flipped.
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```

This script defines a function `flip_case` that takes a string as input, flips the case of each character using the `swapcase` method, and returns the resulting string. The function is then tested with a few examples to demonstrate its usage.