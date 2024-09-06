```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function that returns the count of occurrences of a given substring in the original string, accounting for overlapping occurrences. 
    """
    `string` and `substring` are str objects.
    return sum(1 for i, char in substring if char in string and char not in substring[:i])
```