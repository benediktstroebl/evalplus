```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of occurrences of the substring in the string, 
    including overlapping matches.
    """
    string = "aaaaaaa"
    sub = "aa"
    n = 0
    for char in string:
        if char == sub: n += 1
    return n
```