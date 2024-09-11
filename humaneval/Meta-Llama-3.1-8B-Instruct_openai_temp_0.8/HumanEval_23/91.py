```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The string to get the length of

    Returns:
        int: The length of the string

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
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function is used to get the length of the string. The docstring includes a description, argument information, return information, and examples of how to use the function. The script also includes test cases to demonstrate the function's behavior.