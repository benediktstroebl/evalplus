```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, considering overlapping matches.
    >>> how_many_times('', 'a') # Should return 0
    >>> how_many_times('aaa', 'a') # Should return 3
    >>> how_many_times('aaaa', 'aa') # Should return 3
    """
    return sum((1 for i,eq in enumerate(string.find(substring)))
```