```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  == 3
    >>> how_many_times('aaaa', 'aa') == 3
    """
    return sum(1 for s in string.find(substring, 0, re. singular=True) and s == substring)
```