```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: The string with its case flipped.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a generator expression to iterate over each character in the string, swap its case with `c.swapcase()`, and then joins them back into a string with `join()`. The script also includes example use cases to demonstrate the function's behavior.