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

# Testing the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the number of items in an object. We use docstrings to provide documentation for the function, including a description, parameters, return value, and examples of usage. Finally, we test the function with a few inputs to demonstrate its behavior.