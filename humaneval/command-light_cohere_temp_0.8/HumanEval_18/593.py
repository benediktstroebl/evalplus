```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times('aa', 'a') == 0
    >>> how_many_times('aaaaaaa', 'aa') == 6
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```