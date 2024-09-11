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

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

In this script, we define a function called `strlen` that takes a string as an argument and returns its length. We use Python's built-in `len` function to calculate the length of the string.

The script also includes two test cases to verify that the function works correctly for an empty string and a non-empty string.

To run the script, save it to a file with a `.py` extension (for example, `strlen.py`) and execute it with Python (for example, `python strlen.py`).