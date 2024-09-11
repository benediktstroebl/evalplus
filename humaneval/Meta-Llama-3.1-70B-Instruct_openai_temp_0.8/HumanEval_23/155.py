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

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('hello world'))  # Expected output: 11
```

This Python script defines a function `strlen` that calculates the length of a given string. It uses Python's built-in `len` function to achieve this. The script also includes some test cases to demonstrate the function's usage and verify its correctness.