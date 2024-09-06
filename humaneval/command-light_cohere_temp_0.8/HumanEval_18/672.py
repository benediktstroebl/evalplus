```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of a given substring in the original string,
    considering overlapping cases.
    Example:
    1.
    > return 0
    how many overlapping instances of the substring in the original string.
    """

    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```