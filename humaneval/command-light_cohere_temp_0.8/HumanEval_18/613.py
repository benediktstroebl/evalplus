```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times(''.join', '.')
    0
    >>> how_many_times('abcde', 'de')
    3
    >>> how_many_times('aa', 'aaa')
    0
    >>> how_many_times('aa', 'aaaa')
    3
    """
    count = 0
    for i in string:
        if i == substring:
            count += 1
    return count
```