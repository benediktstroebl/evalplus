```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de')
    3
    >>> how_many_times('  abcdefg   ', 'def')
    3
    >>> how_many_times('abcdefgabcde', 'abcde')
    5
    >>> how_many_times('abcdefgabcde', 'def')
    0
    """
    return sum(1 for i, j in zip(string.split(substring),l))
```