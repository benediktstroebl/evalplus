```python
def strlen(string: str) -> int:
    """
    Returns the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

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

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. It also includes docstrings to provide documentation and examples for the function. The script then tests the function with the specified examples.