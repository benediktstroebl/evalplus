```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while not overlapping.
    >>> string = "aaa"
    >>> how_many_times('a', 'a')
    3
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('bbbb', 'a')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```