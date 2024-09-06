```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, without overlapping.
    >>> string = "aaaaaa"
    sub = "a"
    count = 0
    for i in range(len(string)):
        if string[i] == sub:
            count += 1
    return count
>>> how_many_times('aaaaaa', 'a') #3
```