```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): input string

    Returns:
    int: length of the string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
if __name__ == "__main__":
    print(strlen(""))  # Output: 0
    print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The length of a string in Python is given by the built-in `len` function, which is used here. The docstring explains the purpose of the function, its parameters, its return value, and provides some examples of its usage.