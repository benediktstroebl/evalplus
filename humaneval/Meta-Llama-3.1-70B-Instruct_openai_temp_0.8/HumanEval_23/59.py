```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
assert strlen('') == 0
assert strlen('abc') == 3

if __name__ == "__main__":
    print("All test cases pass")
```

This script defines the `strlen` function, provides documentation for it, includes test cases, and runs the test cases when the script is executed directly. The test cases are implemented using Python's built-in `assert` statement, which will raise an `AssertionError` if the test fails. If all test cases pass, the script will print "All test cases pass".