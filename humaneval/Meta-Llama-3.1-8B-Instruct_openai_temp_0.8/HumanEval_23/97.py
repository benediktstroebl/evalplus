```python
def strlen(string: str) -> int:
    """ Return length of given string

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
```

You can run this script to verify the function's behavior. The `len` function in Python automatically returns the length of a string. This function provides a simple interface for achieving the same result. 

If you need to implement the length calculation manually (for educational purposes or other reasons), you could replace the `return len(string)` line with a loop that counts the characters:

```python
def strlen(string: str) -> int:
    """ Return length of given string

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
    count = 0
    for _ in string:
        count += 1
    return count
```

This manual implementation has a similar effect, but it is less efficient because it requires iterating over all characters in the string.