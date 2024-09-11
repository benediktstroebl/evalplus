```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.
    
    Args:
    string (str): Input string.
    
    Returns:
    int: Length of the input string.
    
    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This Python script defines a function `strlen` that calculates the length of a given string using Python's built-in `len` function. The function includes a docstring with a description, parameters, return value, and examples. The script also includes test cases to demonstrate the function's usage.