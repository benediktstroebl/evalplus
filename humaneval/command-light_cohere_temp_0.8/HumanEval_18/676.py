```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found anywhere in the 
    original string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('bbaaaaa', 'ba')
    0
    """
    count = 0
    for char in substring:
        if char in string:
            count += 1
        if count == len(substring):
            return count
    return 0
```