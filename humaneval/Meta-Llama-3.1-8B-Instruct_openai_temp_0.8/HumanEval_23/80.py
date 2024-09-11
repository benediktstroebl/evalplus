```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to calculate the length of a string. The docstring provides a description of the function, its parameters, and its return value, as well as examples of its usage. The test at the end of the script demonstrates how to call the function with different inputs.