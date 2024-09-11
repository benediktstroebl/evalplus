```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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

This Python script defines a function `strlen` that takes a string as an argument and returns its length using the built-in `len` function. The function is well-documented with a docstring that explains its purpose, arguments, return values, and provides examples of usage. The script also includes test cases to verify the function's correctness.