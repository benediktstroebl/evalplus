```python
def strlen(string: str) -> int:
    """
    Return length of given string.
    
    Args:
    string (str): The input string.
    
    Returns:
    int: The length of the string.
    
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
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function called `strlen` that calculates the length of a given string using Python's built-in `len` function. The docstring provides a clear description of the function's purpose, parameters, return value, and includes example use cases. The script also includes test cases to verify the function's correctness.