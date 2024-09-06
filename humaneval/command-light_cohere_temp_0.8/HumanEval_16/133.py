```python
def count_distinct_characters(string):
    """
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('abcX')
    3
    >>> count_distinct_characters('abcXyz')
    4
    >>> count_distinct_characters('jerry')
    4
    >>> count_distinct_characters('A')
    1
    >>> count_distinct_characters('ZYX')
    2
    """
    return len({c for c in string if c.isalpha()})

```