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
```

In this script, we define a function `strlen` that takes a string as input and returns its length. The `len` function is a built-in Python function that returns the length of a sequence or a collection, which includes strings. The test cases at the end demonstrate the function's behavior with empty and non-empty strings.