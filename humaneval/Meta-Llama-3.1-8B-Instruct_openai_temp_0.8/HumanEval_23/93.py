```python
def strlen(string: str) -> int:
    """Return length of given string.

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


# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, the function `strlen` takes a string as an argument and returns its length using the built-in `len` function in Python. The function is then tested with two examples: an empty string and a string containing three characters.