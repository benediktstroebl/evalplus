```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string,
    counting overlapping matches.
    >>> how_many_times('','a') # 0
    >>> how_many_times('aaa', 'a') # 3
    >>> how_many_times('aaaa', 'aa') # 3
    """
    return sum(1 for i, x in enumerate(string.find(substring), string.find(substring), an=x) > 0)
```