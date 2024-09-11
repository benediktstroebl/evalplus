```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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

# Test cases
print(strlen('') == 0)  # Expected output: True
print(strlen('abc') == 3)  # Expected output: True
```

This script defines a function `strlen` that takes a string as an argument and returns its length using the built-in `len` function. The function includes documentation with a description, argument description, return description, and examples.

The test cases at the end of the script verify that the function works as expected. They compare the function's output to the expected output and print `True` if the outputs match, indicating a successful test.