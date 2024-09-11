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

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This Python script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. The function includes docstrings to describe its purpose, parameters, return type, and examples of usage. The test cases at the end of the script verify the function's correctness.