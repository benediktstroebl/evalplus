```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de')
    3
    >>> how_many_times('abcbaaccb', 'a')
    4
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```