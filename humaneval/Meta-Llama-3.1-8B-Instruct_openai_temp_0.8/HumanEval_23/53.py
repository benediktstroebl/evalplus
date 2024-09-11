```python
def strlen(string: str) -> int:
    """Return length of given string
    
    Args:
        string (str): The input string
    
    Returns:
        int: The length of the string
    
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

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python can be obtained using the built-in `len` function. The script includes docstrings to provide documentation and examples of how to use the function.