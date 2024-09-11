```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

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
assert strlen('') == 0, "Test case 1 failed"
assert strlen('abc') == 3, "Test case 2 failed"
print("All test cases passed.")
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. The script also includes two test cases to verify that the function works correctly. If both test cases pass, it prints "All test cases passed."