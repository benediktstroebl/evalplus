Here's the self-contained Python script that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times a given substring can be found in the original string, considering overlapping matches.
    >>> how_many_times('aaa', 'a') -> 3
    >>> how_many_times('aaaaaaa', 'aaa') -> 6
    """
    count = 0
    start = 0
    length = len(substring)
    while start < len(string):
        if string[start:start+length] == substring:
            count += 1
        start += 1
    return count
```