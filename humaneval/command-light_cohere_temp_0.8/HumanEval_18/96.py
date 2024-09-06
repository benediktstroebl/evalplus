```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, considering case and all characters.
    >>> how_many_times('abcde', 'de')
    3
    """
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count
```