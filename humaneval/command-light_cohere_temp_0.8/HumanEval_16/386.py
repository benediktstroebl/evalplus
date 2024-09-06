```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    """
    return len(dict(c for c in string.isalpha()))
   
   
    """ Test
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('JER')
    4
    """
    return len(dict(c for c in string.isalpha()))
```