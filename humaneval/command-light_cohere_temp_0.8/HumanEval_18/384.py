```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    taking overlapping matches into account.
    >>> how_many_times('aa', 'a') == 3
    """
    return sum(1 for i, x in enumerate(string.find(substring)))
```