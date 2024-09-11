```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): Input string.

    Returns:
        int: Length of the input string.

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
```

In this script, we define the `strlen` function that takes a string as input and returns its length using the built-in `len` function. The docstring provides a description of the function's purpose, its input parameter, and its return value, as well as some examples of how to use it. The script also includes test cases to demonstrate the function's behavior.