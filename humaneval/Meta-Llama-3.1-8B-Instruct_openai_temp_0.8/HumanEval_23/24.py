### Calculating the Length of a String
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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
```

You can run this script in a Python environment to test the function. The function works by simply calling Python's built-in `len` function, which returns the length of any sequence (including strings).

### Testing the Function
```python
# Test the strlen function
print(strlen(''))  # Should print 0
print(strlen('abc'))  # Should print 3
print(strlen('Hello, World!'))  # Should print 13
```