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

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This Python script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python, which returns the number of items in an object. The docstring explains the purpose of the function, its input and output, and provides examples of its usage. The script also includes test cases to verify the correctness of the function.