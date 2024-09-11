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

This script defines the `strlen` function, which takes a string as input and returns its length. The function uses the built-in `len` function to calculate the length of the string. The docstring explains the purpose of the function and provides examples of its usage. The script then tests the function with two examples.