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
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. We include docstrings to provide documentation and test cases to verify the correctness of the function.

To run this script, save it to a file with a `.py` extension (for example, `strlen.py`) and execute it with Python (for example, `python strlen.py`).