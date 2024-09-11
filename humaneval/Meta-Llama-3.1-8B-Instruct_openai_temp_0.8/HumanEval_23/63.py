```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
    # Use built-in len() function to get the length of the string
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen()` that takes a string as input and returns its length. The function uses the built-in `len()` function in Python, which returns the number of items in an object. In this case, it returns the number of characters in the input string. The script also includes docstrings to provide documentation and example usage of the function.