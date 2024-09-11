```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('World'))  # Output: 'wORld'
```

In this script, the `swapcase()` method is used to flip the case of each character in the string. This is a built-in method for strings in Python, making the script simple and efficient.