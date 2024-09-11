```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is calculated using the `len` function, which is a built-in function that returns the number of items in an object. The script also includes test cases to demonstrate the function's behavior.