```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string.

    Returns:
        int: Length of the input string.

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

This script defines a function `strlen` which takes a string as an argument and returns its length. The function uses Python's built-in `len` function to calculate the length of the string. The docstring of the function includes a description, argument information, return information, and test cases. At the end, it tests the function with empty and non-empty strings.