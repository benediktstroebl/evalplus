```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('', 'a')  # 0
    >>> how_many_times('aaa', 'a')  # 3
    >>> how_many_times('aaaa', 'aa')  # 3
    """
    return sum(1 for i, j in zip(string.find(substring), , substring) if j == 0)
```