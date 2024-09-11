```python
def strlen(string: str) -> int:
    """Return length of given string
    
    Args:
        string (str): The string for which the length is to be found.
    
    Returns:
        int: The length of the given string.
    
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

In this script, we define a function `strlen` that takes a string as an argument and returns its length using the built-in `len` function. The docstring explains the purpose of the function, its parameters, return value, and provides examples of its usage. Finally, we test the function with a few examples.