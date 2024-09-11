```python
def strlen(string: str) -> int:
    """Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

In this script, the `strlen` function uses the built-in `len` function in Python to calculate the length of a given string. The `len` function returns the number of items in an object (in this case, a string).