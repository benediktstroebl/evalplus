```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Parameters:
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

In this script, we define a function `strlen` that takes a string as input and returns its length. We use the built-in `len` function in Python to calculate the length of the string. The docstring provides documentation for the function, including its parameters, return value, and examples of usage.