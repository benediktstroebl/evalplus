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

In this script, we define a function `strlen` that takes a string as an input and returns its length using the built-in `len` function in Python. The `len` function returns the number of items in an object, which for strings is the number of characters. We include docstrings to provide documentation for the function and examples of its usage.