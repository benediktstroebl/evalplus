```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

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

In this code, the `strlen` function uses Python's built-in `len` function to calculate the length of a given string. The function includes a docstring that explains its purpose, parameters, and return value, as well as provides example usage. The script also includes test cases to demonstrate the function's behavior.