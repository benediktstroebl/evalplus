```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

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
assert strlen('') == 0
assert strlen('abc') == 3

print("All test cases pass.")
```