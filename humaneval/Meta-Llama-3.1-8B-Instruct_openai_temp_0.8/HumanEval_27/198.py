```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be modified.
    
    Returns:
        str: The modified string with flipped case.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that uses the built-in `swapcase` method of Python strings to flip the case of a given string. The method swaps the case of each character in the string, effectively flipping the case. The script then tests the function with a few examples.