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


# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

This Python script defines a function `strlen` that calculates the length of a given string. The function takes a string as an argument and returns its length using the built-in `len` function. The script also includes test cases to verify the function's correctness. If all test cases pass, it prints "All test cases pass."