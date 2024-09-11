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
    length = 0
    for char in string:
        length += 1
    return length


# Test cases
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
```

However, this problem has a much simpler solution in Python. Here's how you could rewrite it using the built-in `len` function:

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


# Test cases
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
```

The `len` function returns the number of items in an object. When the object is a string, it returns the number of characters in the string. This is the most Pythonic way to get the length of a string.