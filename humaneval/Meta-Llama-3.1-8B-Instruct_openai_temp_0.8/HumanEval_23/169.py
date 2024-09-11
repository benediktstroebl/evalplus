```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

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
print(strlen("Hello World"))  # Output: 11
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The function is then tested with a few examples to demonstrate its usage. The docstring provides a description of the function, its parameters, return value, and some examples of how to use it.