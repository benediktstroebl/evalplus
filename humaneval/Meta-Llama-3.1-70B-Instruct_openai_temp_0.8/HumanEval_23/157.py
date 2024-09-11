Here's a Python script that solves the problem:

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
print(strlen('hello world'))  # Expected output: 11
```

In this script, we define the `strlen` function, which takes a string as input and returns its length using the built-in `len` function in Python. We also include test cases to verify the correctness of the function.