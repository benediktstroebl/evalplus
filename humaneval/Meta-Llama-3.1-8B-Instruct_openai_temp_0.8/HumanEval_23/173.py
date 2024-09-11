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
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. 

The docstring of the function includes a description of what the function does, the input parameter, the return value, and some examples of how to use the function. The last two lines test the function with some example inputs.