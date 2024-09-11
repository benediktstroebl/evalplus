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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This Python script defines a function `strlen` that takes a string as input and returns its length. The `len` function is a built-in Python function that returns the number of items in an object. In this case, it is used to count the number of characters in the input string.

You can run this script to test the `strlen` function with the provided test cases. The expected output is printed as comments next to each test case.