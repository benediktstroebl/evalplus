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

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this code, we define a function `strlen` that takes a string as an input and returns its length. We use the built-in `len` function in Python to calculate the length of the string. The function includes a docstring that provides a description of the function, its arguments, return values, and some examples of how to use it. At the end, we test the function with two examples.