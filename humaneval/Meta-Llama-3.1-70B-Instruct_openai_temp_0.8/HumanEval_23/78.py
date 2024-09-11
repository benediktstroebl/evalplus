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
if __name__ == "__main__":
    assert strlen('') == 0, f"Expected strlen('') to be 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to be 3, but got {strlen('abc')}"
    print("All test cases passed.")
```

This script defines the `strlen` function as specified, and includes two test cases at the end to verify its correctness. The test cases use Python's built-in `assert` statement, which will raise an `AssertionError` if the condition is not met. If the script runs without raising an error, it will print "All test cases passed." to indicate that the function is working as expected.