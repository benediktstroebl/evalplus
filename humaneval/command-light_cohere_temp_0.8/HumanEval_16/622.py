```python
def count_distinct_characters(string):
    """
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('jerry')
    4
    >>> count_distinct_characters('  jerry  ')
    4
    >>> count_distinct_characters('A')
    5
    >>> count_distinct_characters('aa B')
    3
    >>> count_distinct_characters('    jk123 ')
    4
    """
    return len(set(string))
```