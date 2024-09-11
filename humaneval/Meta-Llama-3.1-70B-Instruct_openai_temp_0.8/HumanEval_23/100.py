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
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3

if __name__ == "__main__":
    test_strlen()
    print("All test cases pass")
```

In this script, the `strlen` function uses Python's built-in `len` function to calculate the length of the input string. The `test_strlen` function contains test cases to verify the correctness of the `strlen` function. When you run this script, it will automatically execute the test cases and print "All test cases pass" if all tests pass.