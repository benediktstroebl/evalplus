```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function returns the number of times the given substring can be found in the original string.
    It counts overlapping cases too.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for char in substring:
        count += string.find(char, 0, len(string)) != None
    return count
```