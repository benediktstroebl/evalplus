```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de')
    2
    """
    count = 0
    for char in substring:
        count += string.find(char) != None
    return count
```