### Python Script to Calculate String Length
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

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello world'))  # Output: 11
```
This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The function is then tested with several example inputs to verify its correctness.