Here's the code that contains a self-contained function to find the number of times a given substring can be found in the original string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Should return 3
    >>> how_many_times('aaa', 'aa')  # Should return 3
    >>> how_many_times('aaaaaaa', 'aa')  # Should return 6
    """
    return sum(1 for n in string. contains(substring)
```