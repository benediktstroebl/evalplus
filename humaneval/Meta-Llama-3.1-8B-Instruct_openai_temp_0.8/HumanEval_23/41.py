```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
    string (str): The input string
    
    Returns:
    int: The length of the input string
    
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

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is given by the `len` function, so we simply return the result of calling `len(string)`. The function also includes a docstring that explains its purpose and parameters, and provides some examples of how to use it.