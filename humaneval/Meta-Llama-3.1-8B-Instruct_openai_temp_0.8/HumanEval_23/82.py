```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): The string to calculate the length of.

    Returns:
        int: The length of the given string.

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

This script defines the `strlen` function, which calculates the length of a given string using the built-in `len` function. It also includes docstrings and example usage to demonstrate how the function works. The `print` statements at the end test the function with two different inputs.