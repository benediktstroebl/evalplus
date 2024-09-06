```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while ignoring case and ignoring overlapping occurrences.

    :
    string.lower() and string and substring.
    return sum(1 for char in string if char == substring and substring in string.lower() == substring)
    """
    Example usage:
    >>> how_many_times('aaaaaa', 'aa')
    3
    """
    return sum(1 for char in string if char == substring and substring in string.lower() == substring)
```