```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): input string
    
    Returns:
        int: length of the input string
    
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

This Python script defines a function `strlen` that calculates the length of a given string. It uses the built-in `len` function in Python to achieve this. The script also includes docstrings to provide documentation for the function and examples of its usage.