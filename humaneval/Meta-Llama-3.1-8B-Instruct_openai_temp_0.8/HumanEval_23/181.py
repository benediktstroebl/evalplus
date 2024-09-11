```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
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

This Python script defines a function `strlen` that returns the length of a given string. It uses the built-in `len` function to calculate the length of the string. The docstring provides a description of the function, its arguments, return value, and includes example use cases. The test cases at the end demonstrate how to use the function and verify its correctness.