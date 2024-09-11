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

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. The test cases demonstrate the usage of the function with an empty string and a string with 3 characters.