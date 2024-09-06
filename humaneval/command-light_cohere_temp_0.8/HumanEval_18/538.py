```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string.
    >>> 'aa' in 'aaaaaa'
    4
    >>> 'a' in 'aaaaa'
    True
    """
    return sum(1 for s in string.find(substring, 0, 0))
```