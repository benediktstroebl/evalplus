```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') #3
    >>> how_many_times('aaaa', 'aa') #3
    """
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count
```