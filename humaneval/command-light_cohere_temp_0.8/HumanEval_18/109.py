```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.

    Parameters:
    string: str, the original string
    substring: str, the substring to search for
    Returns: int, the number of positions where substring can be found
    """
    return sum(1 for pos, x in enumerate(string.find(substring, full=True) if x and pos not in string.find(substring, full=False))
```