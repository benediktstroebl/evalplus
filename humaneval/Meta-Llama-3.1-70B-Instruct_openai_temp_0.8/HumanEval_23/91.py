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
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. It also includes two test cases to verify the correctness of the function. If the function passes all test cases, it prints "All test cases pass".