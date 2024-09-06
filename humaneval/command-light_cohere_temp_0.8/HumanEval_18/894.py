```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    considering overlapping occurrences.
    >>> string = 'aaaaaa'
    >>> how_many_times('aa', 'aa')
    3
    """
    return len([x for x in string.find(substring, 0, string.how_many_times(substring, 0)))
```