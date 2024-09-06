```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the substring appears in the original string.

    1. Find all positions of string: Use a simple iterator
    2. Count all occurrences: Use the count and check
    """
    return len([string.find(substring)])
```