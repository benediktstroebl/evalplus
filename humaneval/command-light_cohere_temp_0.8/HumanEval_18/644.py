```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, counting overlapping cases.
    >>> string = "aaaaaaa"
    >>> how_many_times("aaa", "aa")
    3
    >>> string = "abc"
    >>> sub = "a"
    >>> how_many_times(string, sub)
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```