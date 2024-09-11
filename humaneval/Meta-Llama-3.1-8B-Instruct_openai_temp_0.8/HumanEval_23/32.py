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
    # Use built-in len() function to get the length of the string
    return len(string)

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that returns the length of a given string. It uses the built-in `len()` function to achieve this, which makes the code concise and efficient. The docstring provides a clear description of the function's purpose, parameters, and return value, as well as example usage. The script also includes test cases to verify the function's correctness.