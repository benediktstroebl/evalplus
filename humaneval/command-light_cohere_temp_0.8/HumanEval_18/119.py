```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, overlapping allowed.
    Return the count.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('123456', '456')
    4
    >>> how_many_times('123456', '1234')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```