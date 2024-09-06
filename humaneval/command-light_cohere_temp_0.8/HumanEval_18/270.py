```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaaaaaaa'
    >> how_many_times('aaa', 'a')
    4
    >>> 'aaa'
    >> how_many_times('aaa', 'a')
    0
    """
    return len(string.find(substring))
```