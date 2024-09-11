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


# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
print(strlen("Hello, World!"))  # Expected output: 13
```

This Python script defines a function `strlen` that calculates the length of a given string and returns it. The function uses Python's built-in `len` function to get the length of the string. The script also includes test cases to demonstrate the function's behavior.