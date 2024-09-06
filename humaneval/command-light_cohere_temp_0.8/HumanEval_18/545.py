```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """ with the dipping and the string as a substring
    """
    return sum(1 for x in string.find(substring, string))
```