```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlapping cases.
    >>> string = "aaaaaa"
    substring = "aa"
    return len(string.find(substring))
    """

# Example usage
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 6
```