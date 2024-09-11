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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is obtained using the built-in `len` function, which is what the script uses. The docstring explains how to use the function, including examples of how it behaves with different inputs.