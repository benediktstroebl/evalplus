```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
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

This script defines the `strlen` function as requested and includes docstrings for documentation and examples for testing. The function uses the built-in `len` function to get the length of the string. The script also includes test cases to verify that the function works correctly.