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

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses Python's built-in `len` function to calculate the length of the string. The script also includes test cases to verify that the function works as expected.