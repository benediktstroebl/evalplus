```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

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

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python, which returns the number of items in an object. The script also includes docstrings to document the function's behavior and includes some test cases to demonstrate its usage.