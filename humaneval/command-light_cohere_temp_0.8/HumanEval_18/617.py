```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')    #Result: 3
    >>> how_many_times('aaaa', 'aa')  #Result: 3
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```