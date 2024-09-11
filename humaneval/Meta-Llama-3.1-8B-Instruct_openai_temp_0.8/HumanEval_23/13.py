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
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string. The docstring explains the purpose of the function, its input and output, and includes examples of its usage. The script then tests the function with different inputs.