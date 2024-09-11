### String Length Calculator
#### A Simple Python Function

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

This Python function uses the built-in `len` function to calculate the length of a given string. The function takes a string as input and returns its length as an integer. The docstring provides a clear explanation of the function's purpose, arguments, return value, and examples of usage.