```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaaaa', 'aa')
    4
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count
```