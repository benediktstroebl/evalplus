```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """
   
    is the length of the substring and original string, it will return the number of positions where the substring is found.
    """ 
    # Uses the Searches for the substring in the original string using itertools.count(), which will the many times the
    """
    return sum(1 for pos in range(len(string)) if string[pos] == substring)
```