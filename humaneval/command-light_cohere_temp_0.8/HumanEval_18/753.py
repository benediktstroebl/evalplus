```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    :
    overlapping matches are counted.
    """
    using a different cases:
    - exact match
    - case insensitive match
    - different case but same position match
    - different cases
    """
    return sum(1 for char in substring if char in string and char == substring[0])
```