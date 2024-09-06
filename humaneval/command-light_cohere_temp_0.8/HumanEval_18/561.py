```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('aa', 'aaa')
    0
    >>> how_many_times('abcdeabcde', 'abcde')
    5
    >>> how_many_times(''.joinabcdeabcde', 'abcde')
    3
    """
    return sum(1 for i, j in zip(string, substring) if j == string[i])
```