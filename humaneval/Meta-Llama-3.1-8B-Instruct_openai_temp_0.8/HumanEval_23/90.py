```python
def strlen(string: str) -> int:
    """
    Returns the length of the given string.

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
print(strlen(''))  # Should print: 0
print(strlen('abc'))  # Should print: 3
print(strlen('hello world'))  # Should print: 12
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python, which returns the number of items in an object. The script also includes test cases at the end to demonstrate the function's usage.