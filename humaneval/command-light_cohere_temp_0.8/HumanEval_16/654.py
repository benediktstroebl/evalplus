```python
def count_distinct_characters(string: str):
    """ 
    Returns the number of distinct characters in the given string, 
    regardless of case.
    """
    return len([char for char in string.strip.lower() if len()])

    """ 
    Example usage:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len([char for char in string.lower() if len(char)])
```