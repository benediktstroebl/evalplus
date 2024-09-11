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

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello world'))  # Output: 11
```

In this code, the function `strlen` takes a string as input and returns its length using the built-in `len` function. The docstring provides a description of the function, its parameters, return value, and examples of usage.