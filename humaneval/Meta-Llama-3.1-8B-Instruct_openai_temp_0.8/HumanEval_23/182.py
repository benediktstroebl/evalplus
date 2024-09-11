```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the string

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

However, if you want to implement the `strlen` function manually without using the built-in `len` function, you can do it like this:

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    length = 0
    for _ in string:
        length += 1
    return length

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This version of the `strlen` function works by iterating over each character in the string and incrementing the length counter for each one.