```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Return 3 since 'aaa' can be found 3 times in 'aaa'
    """
    return len(string.find(substring))
```