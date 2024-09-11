```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function to achieve this. The docstring provides a description of the function, its arguments, and its return value, as well as some examples of how to use it. Finally, it includes some test cases to verify that the function works correctly.