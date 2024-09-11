```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length. We use the built-in Python function `len` to calculate the length of the string. The function is then tested with two example inputs.