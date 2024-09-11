```python
def strlen(string: str) -> int:
    """
    Return length of given string.
    
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
    # The built-in len function in Python returns the length of a string
    return len(string)

# Test the strlen function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python, which is efficient and Pythonic. The docstring provides a description of the function, its parameters, and its return value, as well as some examples of how to use it.