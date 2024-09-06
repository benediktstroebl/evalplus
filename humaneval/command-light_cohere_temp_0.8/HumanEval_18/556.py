```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')    # returns 3
    >>> how_many_times('aaaaaaa', 'aa')  # returns 4
    """
    return sum(1 for s in string.find(substring, 0, re.
)(substring))
```