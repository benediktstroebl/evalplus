```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string.

    Returns:
        int: Length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

In this script, the built-in Python function `len()` is used to find the length of the input string. This function works with most built-in Python data types, including strings, lists, tuples, dictionaries, and sets.

You can test this function using the provided example use cases:
```python
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```