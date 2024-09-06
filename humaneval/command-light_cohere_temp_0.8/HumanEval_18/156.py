```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaaaaa' == how_many_times('aaa', 'aa')
    True
    >>> 'abccd' == how_many_times('abcd', 'cd')
    True
    >>> 'wwwwevw' == how_many_times('www', 'wevw')
    True
    >>> 'abcde' == how_many_times('abcde', 'de')
    False
    """
    return len([i for i, char in enumerate(string) if char == substring])
```