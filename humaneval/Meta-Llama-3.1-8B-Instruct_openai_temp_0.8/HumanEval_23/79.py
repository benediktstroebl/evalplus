```python
def strlen(string: str) -> int:
    """Return the length of the given string.

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
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello'))  # Output: 5
```

In this script, we define a function `strlen` that takes a string as input and returns its length. The length of a string is calculated using the built-in `len` function in Python. The docstring explains the purpose and usage of the function, as well as provides some examples of how to use it. Finally, we test the function with some example inputs.