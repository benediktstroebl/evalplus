```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that finds the count of occurrences of a substring in the original string.
    >>> string = 'aaaaaaa'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    == 3
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```