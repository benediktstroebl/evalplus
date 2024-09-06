```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds the number of times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Should return 3
    >>> how_many_times('aaaa', 'aa')  # Should return 3
    >>> how_many_times('apple pie', 'pie')  # Should return 1
    >>> how_many_times('abcdeABCDEFabcde', 'abcde')  # Should return 5
    >>> how_many_times('abcdefghijklmnopqrstuvwxyz', 'ABC')  # Should return 13
    """
    count = 0
    for i in string:
        if substring in i:
            count += 1
    return count
```