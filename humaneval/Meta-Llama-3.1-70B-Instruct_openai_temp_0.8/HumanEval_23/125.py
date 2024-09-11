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

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('hello world'))  # Expected output: 11
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of usage. The script also includes test cases to verify the function's correctness.