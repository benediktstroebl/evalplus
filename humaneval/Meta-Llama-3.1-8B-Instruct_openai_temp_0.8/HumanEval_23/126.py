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
    return len(string)

# Test the function
print(strlen(''))   # Expected output: 0
print(strlen('abc')) # Expected output: 3
```

This script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. It includes docstrings for documentation and provides example use cases in comments. The script also includes a test at the end to demonstrate how to use the function.