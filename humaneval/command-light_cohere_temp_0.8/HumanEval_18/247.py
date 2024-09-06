```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    while avoiding overlapping occurrences.
    >>> string = "aaaaaaa"
    >>> how_many_times('a', 'a')
    3
    >>> how_many_times('aaaaaaa', 'a')
    4
    """
    count = 0
    start = 0
    end = len(string) - 1
    while start <= end:
        current = string[start:end]
        if current == substring: 
            count += 1
        start += 1
    return count
```