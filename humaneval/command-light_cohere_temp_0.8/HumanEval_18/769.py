```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    considering overlapping matches.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aaa')
    3
    """
    count = 0
    for char in substring:
        count += string.find(char) != None
    return count
```