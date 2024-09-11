### Python Script to Calculate String Length

```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print("Length of empty string:", strlen(""))  # Expected output: 0
print("Length of 'abc' string:", strlen('abc'))  # Expected output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. We then test this function with two examples: an empty string and a string with three characters.