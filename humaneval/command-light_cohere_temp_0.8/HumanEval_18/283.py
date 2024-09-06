```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('aa', 'aaa')
    0
    >>> how_many_times('abca', 'ab')
    2
    """
    return len([x for x in string.find(substring, 0)])
```