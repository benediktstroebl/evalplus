```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') # Should return 3
    >>> how_many_times('aaaa', 'aa') # Should return 3
    """
    return sum(1 for i, match in enumerate(string.find(substring), string.find(substring), how_many_times(substring, string)))
```