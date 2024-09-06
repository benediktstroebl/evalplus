```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times('abcda', 'a')
    2
    >>> how_many_times('aaa', 'aa')
    3
    >>> how_many_times('  abcdabcda  ', 'a')
    3
    >>> how_many_times('  ab++cd++ab', 'a')
    2
    >>> how_many_times('aa', 'aaaa')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```