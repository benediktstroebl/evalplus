```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> string = "aaaaaaa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    3
    >>> string = ""
    >>> substring = "a"
    >>> how_many_times(string, substring)
    0
    >>> string = "aa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    1
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```