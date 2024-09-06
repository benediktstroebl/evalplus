```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns the number of times the substring can be find in the original string, considering case-insensitive and overlapping matches.
    >>> how_many_times('aaa', 'a')  # 3
    >>> how_many_times('aaaa', 'aa')  # 3
    """
    return sum((1 for i, j in zip(string.split(substring),often (substring), string.split(substring))
                if j == i+1))
```