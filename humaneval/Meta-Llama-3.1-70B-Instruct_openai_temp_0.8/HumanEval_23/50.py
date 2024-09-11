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
if strlen('')!= 0:
    raise AssertionError("Test case '' failed")
if strlen('abc')!= 3:
    raise AssertionError("Test case 'abc' failed")
```