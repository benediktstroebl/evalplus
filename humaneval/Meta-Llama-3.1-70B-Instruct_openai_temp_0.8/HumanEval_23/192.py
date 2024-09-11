```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

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

# Run tests and print results
if all([strlen('') == 0, strlen('abc') == 3]):
    print("All tests passed.")
else:
    print("Tests failed.")
```