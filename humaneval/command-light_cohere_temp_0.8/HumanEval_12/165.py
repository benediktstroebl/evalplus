```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    """
    list must be empty, or contain strings of any length, non-None.
    return the longest in list with the maximum length, or None if the list is empty.
    """
    list must contain only strings
    """
    return max(strings) if strings else None
```

This code solves the problem of finding the longest string in a list of strings, using the `max()` function to find the maximum length. The function works with any list of strings, including strings of any length and returning the longest string in the list or `None` if the list is empty.