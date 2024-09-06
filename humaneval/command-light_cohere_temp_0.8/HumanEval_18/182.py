Here is a self-contained Python function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaaaaa' == how_many_times('aaaa', 'aa')
    True
    """
    return len({i: True for i, _ in enumerate(string) if i == substring})
```