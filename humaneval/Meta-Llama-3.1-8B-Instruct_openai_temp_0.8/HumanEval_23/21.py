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
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. The docstring explains how to use the function and provides example use cases. The test cases at the end demonstrate how to call the function and verify its output.