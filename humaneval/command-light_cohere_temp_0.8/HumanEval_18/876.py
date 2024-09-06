```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function returns the number of occurrences of a given substring in the original string.
    """
    string = 'aaaaaa'
    sub = 'a'
    n = 0
    i = 0
    while i < len(string):
        if string[i] == sub:
            n += 1
        i += 1
    return n
```