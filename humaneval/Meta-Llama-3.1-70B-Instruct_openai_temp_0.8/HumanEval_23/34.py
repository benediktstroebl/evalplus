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


# Test the function
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All tests passed.")
```

This script defines the `strlen` function as per the given problem and includes two unit tests to verify its correctness. If you run this script, it will print "All tests passed." if both tests pass.