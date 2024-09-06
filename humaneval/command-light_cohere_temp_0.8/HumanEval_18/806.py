```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de')
    3
    >>> how_many_times('0000000aaa', 'aaa')
    10
    >>> how_many_times(' Atlantis', 'Al')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```