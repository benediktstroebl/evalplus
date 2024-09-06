```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    >>> string = 'aaaaaaa'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    3
    >>> string = 'abca'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```