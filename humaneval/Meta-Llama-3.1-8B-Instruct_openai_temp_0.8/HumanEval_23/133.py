```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: Length of the input string

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test cases
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
print(strlen("hello world"))  # Output: 11
```

This script defines a function `strlen` that calculates the length of a given string. It includes input validation to ensure the input is a string, and it provides docstrings and example use cases for clarity. The script also includes test cases at the end to demonstrate the function's usage.