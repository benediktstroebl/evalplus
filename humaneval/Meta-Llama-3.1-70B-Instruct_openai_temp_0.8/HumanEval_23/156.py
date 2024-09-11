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
    raise AssertionError("strlen('')!= 0")
if strlen('abc')!= 3:
    raise AssertionError("strlen('abc')!= 3")
print("All test cases passed.")
```