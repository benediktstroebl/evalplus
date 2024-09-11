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
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```

In this script, I've implemented the `strlen` function using the built-in `len` function in Python, which returns the length of any sequence, including strings. The function takes a string as input and returns its length as an integer. The docstring has been updated to include a description of the function, its arguments, and its return values, as well as some examples of usage.