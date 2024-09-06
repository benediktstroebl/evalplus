```python
def count_distinct_characters(string: str):
    """
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    >>> count_distinct_characters('abcABC')
    5
    >>> count_distinct_characters('abc')
    5
    >>> count_distinct_characters('A')
    5
    >>> count_distinct_characters('a')
    4
    >>> count_distinct_characters('fds')
    2
    >>> count_distinct_characters('  jerry')
    2
    >>> count_distinct_characters('  fds123')
    2
    >>> count_distinct_characters('   jerry  ')
    2
    """
    return len(set(string))
```