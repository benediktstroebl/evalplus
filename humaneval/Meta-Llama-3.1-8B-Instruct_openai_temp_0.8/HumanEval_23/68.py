```python
def strlen(string: str) -> int:
    """Return length of given string.

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
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, the `strlen` function uses the built-in `len` function to get the length of the input string. The function is then tested with some example inputs to demonstrate its usage.