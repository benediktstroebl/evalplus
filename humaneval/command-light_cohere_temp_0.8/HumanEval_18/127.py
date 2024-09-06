Here's the self-contained Python function:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('a', 'aa')
    2
    >>> how_many_times('abcde', 'abc')
    4
    >>> how_many_times('abcdaacbc', 'a')
    6
    """
    return len({ i : 0 for i, c in enumerate(string) if c == substring})
```