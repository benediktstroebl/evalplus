```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: Length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This script defines a function `strlen` that calculates the length of a given string. It checks if the input is indeed a string and raises a `TypeError` if it's not. The function uses the built-in `len` function to calculate the length of the string. The example usage at the end demonstrates how to call the function with different inputs.