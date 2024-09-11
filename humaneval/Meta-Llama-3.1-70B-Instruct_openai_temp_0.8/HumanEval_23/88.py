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
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('hello world') == 11
    print("All test cases pass")
```

This script defines a `strlen` function that takes a string as input and returns its length using Python's built-in `len` function. It includes test cases to ensure the function works correctly. When run, the script will print "All test cases pass" if all tests pass.