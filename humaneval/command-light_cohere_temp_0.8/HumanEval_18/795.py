```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    >>> string = "aaaaaaa"
    >>> how_many_times('aa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```