```python
# Self-contained Python script to calculate the length of a given string

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
print("Length of empty string:", strlen(''))
print("Length of 'abc':", strlen('abc'))
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. It also includes docstrings to provide documentation for the function and examples of how to use it. The script then tests the function with two examples.