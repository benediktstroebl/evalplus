```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') == 3
    >>> how_many_times('aaaaaaa', 'aa') == 6
    """
    return len(string.find(substring))
```