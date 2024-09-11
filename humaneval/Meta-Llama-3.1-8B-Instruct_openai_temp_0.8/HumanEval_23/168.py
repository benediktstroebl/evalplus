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

    # Check if input is a string
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")

    # Return the length of the string
    return len(string)


# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This Python script defines a function `strlen` that calculates the length of a given string. It handles edge cases where the input is not a string, raising a `TypeError` in such situations. The function uses Python's built-in `len` function to calculate the length of the string. The code includes example use cases as comments to demonstrate its functionality.