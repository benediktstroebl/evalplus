```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    This using the count-overlapping cases.
    """
    example usage:
    >>> how_many_times('aaaaaaa', 'aa')
    3
    """
    return sum((1 for i, x in enumerate(string.find(substring),last()) if x == substring)
    )
```