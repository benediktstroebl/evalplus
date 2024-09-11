```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Testing the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as an argument and returns its length. The `len` function in Python is used to get the length of a string, which is a built-in feature of the language, making this function very simple. The function includes docstrings to provide documentation and example usage. The script also includes some test cases to demonstrate the function's behavior.