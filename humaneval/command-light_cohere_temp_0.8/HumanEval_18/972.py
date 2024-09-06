```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abcdaaaaa', 'abc')
    2
    >>> how_many_times('abcde', 'abc')
    0
    """
    count = 0
    for i in string:
        if i == substring:
            count += 1
    return count
```