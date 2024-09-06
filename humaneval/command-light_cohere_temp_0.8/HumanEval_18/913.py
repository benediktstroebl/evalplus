```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the substring can be found in the original string.
    For example:
    >>> how_many_times('aaaaaa', 'aa')
    6
    >>> how_many_times('abcdef', 'abc')
    4
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```