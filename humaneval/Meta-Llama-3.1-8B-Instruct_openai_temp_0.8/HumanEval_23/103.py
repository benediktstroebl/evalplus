```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
    string (str): The input string to find the length of.
    
    Returns:
    int: The length of the input string.
    
    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is calculated using the built-in `len` function. The function is then tested with two example use cases.