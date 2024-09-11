```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
if __name__ == "__main__":
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All test cases pass")
```

You can run this script directly. The test cases are included at the end, and they will print an error message if any of the expected results are not met.