### String Length Function
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
    # Check if input is a string
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")

    # Return the length of the string using built-in len() function
    return len(string)

# Test the strlen function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. It also includes error checking to ensure the input is a string. The function is tested with two examples.