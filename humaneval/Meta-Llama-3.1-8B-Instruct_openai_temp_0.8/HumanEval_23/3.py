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

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. The function is documented with a docstring that includes a description, arguments, return value, and examples. The script also includes test cases to demonstrate the function's usage.