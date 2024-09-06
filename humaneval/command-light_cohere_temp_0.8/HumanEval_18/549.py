```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of a substring in the original string, 
    handling overlapping matches and returning the count.
    >>> string = "This is a test string"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    2
    >>> string = "aaaaaa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    4
    >>> string = "This is not valid"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    0
    """
    return sum((1 if (string.find(substring) else 0) for string in string.findall(substring))
```