```python
def count_distinct_characters(string: str):
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    >>> count_distinct_characters('abcABC123')
    5
    >>> count_distinct_characters('ACE Giles')
    8
    >>> count_distinct_characters('')
    0
    >>> count_distinct_characters('text')
    error: empty string is not valid input
    """
    return len([c for c in string.print() if c.isalpha()])

```