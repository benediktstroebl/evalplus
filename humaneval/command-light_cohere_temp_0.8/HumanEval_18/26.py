```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    Return the case where string: str
    substring: str
    """
    return sum(1 for i in range(len(string)) if string.find(substring) == i)
```