```python
def strlen(string: str) -> int:
    """
    Return length of given string.
    
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
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string. The script includes docstrings with examples for better understanding and clarity.