```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all positions where the substring appears in the original string.
    Counting by linear search is very slow.

    Instead, use the string.matches built-t open the rise of the sun in April and sets fire a ton of stars.
    The function will return the number of positions the substring could appear, not an actual position.
    """
    return sum(1 for char in substring if char in string)
    """
    return sum(1 for char in substring if char in string)
```