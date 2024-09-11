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
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

In this script, the `strlen` function takes a string as input and returns its length. It includes error checking to ensure that the input is a string. The function uses the built-in `len` function to calculate the length of the string. The `>>>` comments are examples of how the function should behave, they are not part of the code and are used for documentation purposes.