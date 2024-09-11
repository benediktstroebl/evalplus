### Length of a String in Python
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```
This Python script defines a function `strlen` that takes a string as input and returns its length. The `len` function is used to calculate the length of the string. The function also includes docstrings to provide documentation and examples of usage. The script includes test cases to verify the function's correctness.