```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while avoiding overlapping occurrences.
    >>>
    string: The original text
    >>> substring: The substring to search for
    >>> string = "aaaaaaa"
    >>> how_many_times(string, substring)
    3
    """
    return len([x == substring for x in string])
```