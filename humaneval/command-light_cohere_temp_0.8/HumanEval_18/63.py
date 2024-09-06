```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Purpose: Finds how many times a given substring can be found in the original string, 
    counting overlapping matches.

    Returns: number of occurrences of the substring in the string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aaa')
    6
    """
    occurrences = string.count(substring)
    return occurrences
```