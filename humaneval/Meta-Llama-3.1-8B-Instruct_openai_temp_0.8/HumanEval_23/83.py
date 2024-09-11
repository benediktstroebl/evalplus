```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): input string

    Returns:
        int: length of the input string

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

In this code, we define a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of any sequence (like a string or a list). The function includes documentation with examples to demonstrate its usage. We then test the function by calling it with empty and non-empty strings and print the results.