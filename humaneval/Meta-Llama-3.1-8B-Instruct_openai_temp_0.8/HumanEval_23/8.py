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

# Test cases
print(strlen(""))  # Expected: 0
print(strlen("abc"))  # Expected: 3
```

This Python script defines the `strlen` function that returns the length of the input string. It uses the built-in `len` function in Python to calculate the length. The docstring provides a description of the function, its parameters, and its return value, as well as some examples of how to use it. Finally, it includes test cases to demonstrate the function's correctness.