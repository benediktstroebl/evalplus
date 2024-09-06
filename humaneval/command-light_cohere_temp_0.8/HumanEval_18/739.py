```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of a given substring in a string, with overlapping cases.
    >>> string = "aaaaaaa"
    sub = "aa"
    count = how_many_times(string, sub)
    print(f"The substring {sub} can be found {count} times.")
    """
    return len({i: string.contains(substring) for i,substring in enumerate(substring)})
```