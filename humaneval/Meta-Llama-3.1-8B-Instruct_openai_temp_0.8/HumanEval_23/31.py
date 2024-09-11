```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Example:
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

In this code:

1.  We define a function `strlen` that takes a string as input and returns its length.
2.  The function uses the built-in `len` function in Python, which returns the number of items in an object.
3.  We include a docstring to provide documentation for the function, including its arguments, return value, and example usage.
4.  We test the function with two example use cases.