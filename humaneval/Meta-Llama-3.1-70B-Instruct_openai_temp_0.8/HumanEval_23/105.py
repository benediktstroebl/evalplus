```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

However, please note that this function is redundant as the built-in `len` function in Python can already achieve the same result. The `strlen` function would be more useful if it provided additional error checking or handled non-string inputs, for example:

```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Raises:
        TypeError: If the input is not a string.

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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
try:
    print(strlen(123))  # Expected output: TypeError
except TypeError as e:
    print(e)  # Expected output: Input must be a string
```