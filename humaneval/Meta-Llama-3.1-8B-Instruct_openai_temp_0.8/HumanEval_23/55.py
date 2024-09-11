### Length of a String
#### A self-contained Python script

```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): The input string.

    Returns:
        int: Length of the string.

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

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of the string. The function is documented with a docstring that explains its purpose, arguments, return value, and provides examples of usage. The script also includes test cases to verify the correctness of the function.