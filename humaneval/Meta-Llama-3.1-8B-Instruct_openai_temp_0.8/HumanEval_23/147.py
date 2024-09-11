```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
print(strlen("Hello, World!"))  # Output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string. The script also includes docstrings to provide documentation for the function and test cases to ensure it works correctly.