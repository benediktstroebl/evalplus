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

print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This Python script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. The script also includes docstrings to provide documentation for the function and examples of how to use it.