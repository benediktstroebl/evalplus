```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abcde', 'abc')
    4
    >>> how_many_times('abcba', 'abc')
    3
    >>> how_many_times('abcdef', 'abc')
    5
    >>> how_many_times('', 'a')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```