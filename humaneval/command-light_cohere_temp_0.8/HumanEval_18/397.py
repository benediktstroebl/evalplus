```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') == 3
    >>> how_many_times('aaaa', 'aa') == 3
    True
    """
    return len(string.find(substring))
```