```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function returns the number of occurrences of a given substring within the original string, 
    accounting for case-sensitive and case-overlapping matches.
    >>> how_many_times('aaa', 'a') == 3
    """
    return sum(1 for i,j in zip(string.find(substring, 0), string.find(substring, 0)))
```