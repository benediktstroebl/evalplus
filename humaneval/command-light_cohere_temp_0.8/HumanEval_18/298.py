```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, without overlapping.
    """

    count = 0
    for char in substring:
        if char in string and string.find(char, string):
            count += 1
    return count
    return 0
```