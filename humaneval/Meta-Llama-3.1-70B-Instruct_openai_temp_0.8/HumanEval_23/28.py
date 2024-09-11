```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string.

    Returns:
        int: Length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases
print(strlen('') == 0)  # Expected output: True
print(strlen('abc') == 3)  # Expected output: True
```

This script defines a function `strlen` that calculates the length of a given string. It uses Python's built-in `len` function to achieve this. The function includes a docstring that describes what the function does, its arguments, return value, and provides example usage. The test cases at the end verify that the function behaves as expected.