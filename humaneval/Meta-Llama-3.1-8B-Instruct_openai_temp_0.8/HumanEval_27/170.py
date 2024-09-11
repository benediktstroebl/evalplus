```python
def flip_case(string: str) -> str:
    """ Flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case flipped.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Example usage:
print(flip_case('Hello'))  # Outputs: hELLO
print(flip_case('hELLO'))  # Outputs: HELLO
print(flip_case('abcdefGHI'))  # Outputs: ABCDEFghi
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The `swapcase` method is used to achieve this. The `join` method is used to concatenate the characters back into a single string. The function is then tested with some example inputs.