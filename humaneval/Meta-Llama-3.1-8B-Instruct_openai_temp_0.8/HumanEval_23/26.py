```python
def strlen(string: str) -> int:
    """Return length of given string

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


# Testing the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

Alternatively, if you want to implement it manually without using the built-in `len` function, you could do it like this:

```python
def strlen(string: str) -> int:
    """Return length of given string

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
    length = 0
    for _ in string:
        length += 1
    return length


# Testing the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```