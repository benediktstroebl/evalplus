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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```
This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. The function is well-documented with a docstring that includes a description, argument and return type information, and examples of usage. The script also includes test cases to verify the correctness of the function.