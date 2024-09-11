```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases passed.")
```

This script defines the `strlen` function, which simply returns the length of the input string using the built-in `len` function. The test cases are implemented using assertions, which will raise an `AssertionError` if any of the test cases fail. If all test cases pass, it prints "All test cases passed."