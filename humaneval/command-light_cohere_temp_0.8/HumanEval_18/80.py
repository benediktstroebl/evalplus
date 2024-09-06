```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within the original string,
    considering case-insensitive matches.
    """

   
    for char in substring:
        if string.index(char, 0, < 0:
            continue
        if string.index(char, 0) >= len(string):
            return 0
        string = string.replace(char) + string
    else:
        return how_many_times(string, substring[:-index(char)]) + 1
    return 0
```