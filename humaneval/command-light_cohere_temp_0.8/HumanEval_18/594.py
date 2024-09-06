```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    taking into account overlapping substrings.
    >>> how_many_times('abcda', 'a')
    0
    >>> how_many_times('abcddaaa', 'a')
    3
    """
    return sum(1 for s in string.find(substring, 0, string. result(substring)) )
```