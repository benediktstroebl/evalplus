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

# Test the function
print(strlen(""))  # Should print: 0
print(strlen("abc"))  # Should print: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function is used to get the length of the string. The docstring explains how to use the function and provides examples of its usage, as per the problem statement. The function is then tested with two examples.