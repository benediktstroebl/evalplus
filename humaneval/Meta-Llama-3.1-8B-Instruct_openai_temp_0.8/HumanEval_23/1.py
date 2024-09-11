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
print(strlen("hello world"))  # Output: 11
```

In this script, we define a function `strlen` that takes a string as an argument and returns its length. We use the built-in `len` function to calculate the length of the string. The docstring provides a description of the function, its arguments, and its return value. It also includes examples of how to use the function. The script then tests the function with a few examples.