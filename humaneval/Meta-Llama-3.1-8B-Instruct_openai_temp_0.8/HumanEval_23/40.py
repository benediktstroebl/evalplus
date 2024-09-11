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

# Example usage:
print(strlen('Hello, World!'))  # Output: 13
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. The examples at the end demonstrate how to use the function and show its output for different inputs.