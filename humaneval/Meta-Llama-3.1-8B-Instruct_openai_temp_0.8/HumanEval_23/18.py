```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
    string (str): The input string

    Returns:
    int: The length of the input string

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

In this code, the `strlen` function takes a string as input and returns its length using the built-in `len` function. The docstring explains the purpose of the function, its parameters, and its return value. The function is then tested with two examples.