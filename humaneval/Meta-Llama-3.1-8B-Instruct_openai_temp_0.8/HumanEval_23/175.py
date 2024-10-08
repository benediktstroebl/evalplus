```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): Input string
    
    Returns:
        int: Length of the input string
    
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

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of the string. The docstring provided explains the purpose of the function, its input and output parameters, and provides example usage.