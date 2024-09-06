```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a') == 3 
    """
    return len(string.find(substring))
```