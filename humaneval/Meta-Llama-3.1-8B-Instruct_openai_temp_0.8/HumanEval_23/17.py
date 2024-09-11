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
    return len(string)
```

You can run this script in your Python environment to see the example usage. Note that the `len()` function is a built-in Python function that returns the length of a sequence (such as a string). The `strlen()` function here simply delegates this operation to `len()`, making it a more explicit and readable version of the original code.