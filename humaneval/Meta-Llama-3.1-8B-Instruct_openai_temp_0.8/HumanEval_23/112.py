### String Length Calculator
#### A Simple Python Function to Calculate the Length of a Given String

```python
def strlen(string: str) -> int:
    """
    Returns the length of the given string.

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

# Test the function with example inputs
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes an input string and returns its length. The `len` function in Python is used to get the length of a string. The docstring provides a description of the function, its parameters, and return value, as well as some example use cases.