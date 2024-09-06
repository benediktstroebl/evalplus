```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts the number of occurrences of a substring in the original string, while allowing for overlapping matches.
    >>> string = "aaaaaa"
    >>> how_many_times("aaa", "a")
    3
    >>> how_many_times("aaaa", "aa")
    3
    >>> how_many_times("abcdefghijklmnopqr", "ace")
    2
    >>> how_many_times("abcdefghijklmnopqr", "cc")
    0
    """
    return sum(1 for char in substring if char in string)
```