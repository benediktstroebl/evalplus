```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: Length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length. We use the built-in `len` function in Python to calculate the length of the string. The function includes a docstring that provides a description of the function, its arguments, and its return value, as well as some examples of how to use it. We also include some test code at the end to demonstrate the function's behavior.