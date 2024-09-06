```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> string = "aaaaaa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    3
    >>> string = ""
    >>> substring = "a"
    >>> how_many_times(string, substring)
    0
    >>> string = "aa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    2
    """
    return len({x:0 for x in string.count(substring)})
```