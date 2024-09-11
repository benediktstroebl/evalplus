```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The length of the string.
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

In this script, the `strlen` function takes a string as input and returns its length using the built-in `len` function. The docstring provides documentation for the function, including a description, argument information, return information, and examples of usage.