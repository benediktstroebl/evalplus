```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('', 'a') # Output: 0
    >>> how_many_times('aaa', 'a') # Output: 3
    >>> how_many_times('aaaa', 'aa') # Output: 3
    """
    return sum(1 for s in string.Search(substring))
```