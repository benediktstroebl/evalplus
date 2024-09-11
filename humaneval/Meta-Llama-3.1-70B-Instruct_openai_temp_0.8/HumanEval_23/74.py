```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
    assert strlen('hello world') == 11
    print("All test cases pass")
```

In this script, we define a function `strlen` that takes a string as input and returns its length. We use the built-in `len` function to calculate the length. We also include some test cases to verify that the function works as expected. If all test cases pass, it prints "All test cases pass".