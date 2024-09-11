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
    return len(string)


# Test cases
print(strlen(""))  # Should print 0
print(strlen("abc"))  # Should print 3
```

However, Python already has a built-in function `len()` that can be used to get the length of a string. This can be used to simplify the above code to:

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
    return len(string)


# Test cases
print(strlen(""))  # Should print 0
print(strlen("abc"))  # Should print 3
```