```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') == 3
    >>> how_many_times('aaaa', 'aa') == 3
    """
    return len({ i: 1 for i, char in enumerate(string) if char == substring })
```