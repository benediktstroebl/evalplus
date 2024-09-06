```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function counts how many times a given substring can be found in the original string, 
    considering case-insensitive matching and overlapping occurrences.
    >>> how_many_times('abcde', 'abcde')
    3
    >>> how_many_times('abcba', 'abc')
    3
    >>> how_many_times('aa', 'aaa')
    0
    >>> how_many_times('aaaaaa', 'aaa')
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```