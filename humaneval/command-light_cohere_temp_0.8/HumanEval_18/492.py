```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('', '') == 0
    >>> how_many_times('aaa', '') == 0
    True
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('iiiisiaaa', 'ia')
    3
    >>> how_many_times('iiiiiii', 'ii')
    3
    """
    n = string.count(substring)
    return n
```