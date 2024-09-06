```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    >>> string = "aaaaaaarggherehh
    sub = "aa"
    return len([i for i,x in enumerate(string) if x == sub]) + 1
```