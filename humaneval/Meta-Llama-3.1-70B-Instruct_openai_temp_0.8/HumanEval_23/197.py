```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines the `strlen` function, which uses Python's built-in `len` function to calculate the length of the input string. The function includes a docstring with a description, parameter documentation, return value documentation, and examples of usage. The script also includes test cases to verify the function's correctness.