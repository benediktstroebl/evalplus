```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test cases
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

Note: I've used the built-in Python function `len()` to get the length of the string. This is more efficient and Pythonic than manually counting the characters in the string.