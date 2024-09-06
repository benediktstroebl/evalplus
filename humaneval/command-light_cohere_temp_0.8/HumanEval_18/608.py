```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find the number of times the given substring can be found in the original string.
    >>> how_many_times('aaaaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```