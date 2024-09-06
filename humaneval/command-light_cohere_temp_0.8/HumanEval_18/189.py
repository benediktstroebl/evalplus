```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, overlapping cases
    included.
    Return the count
    the number of occurrences of the substring in the original string.
    """ 
    return sum(1 for char in substring if char in string)
```