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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

In this script, the `strlen` function takes a string as input and returns its length using the built-in `len` function in Python. The function also includes docstrings that provide documentation and examples for how to use the function. The test cases at the end demonstrate how to use the function.