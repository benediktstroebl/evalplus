```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # <-- returns 3
    >>> how_many_times('aaaaaaa', 'aa')  # <-- returns 4
    """
    if not substring:
        raise ValueError("Invalid substring")
    count = 0
    length = len(string)
    for i in range(length):
        if string[i] == substring:
            count += 1
    return count
```