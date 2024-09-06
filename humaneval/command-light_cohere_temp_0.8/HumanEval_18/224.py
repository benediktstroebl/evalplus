Here is a self-contained Python script with a function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('YYYYY', 'Y')
    5
    >>> how_many_times('ababbab', 'ab')
    2
    """
    return len([c == substring for c in string])
```