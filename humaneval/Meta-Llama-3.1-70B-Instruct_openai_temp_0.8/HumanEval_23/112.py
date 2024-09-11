```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
    string (str): Input string.

    Returns:
    int: Length of the input string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
assert strlen('') == 0
assert strlen('abc') == 3
print("All tests passed.")
```
This script defines a function `strlen` that calculates the length of a given string using the built-in `len` function in Python. It includes two unit tests to verify the correctness of the function. If the function works correctly, it prints "All tests passed."