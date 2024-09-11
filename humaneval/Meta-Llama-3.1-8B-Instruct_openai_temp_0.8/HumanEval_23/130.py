```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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

# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

In this script, the `strlen` function takes a string as input and returns its length using the built-in `len` function in Python. The docstring explains the function's purpose, parameters, and return value, including examples of how to use it. The test cases at the end demonstrate the function's behavior with different input strings.