```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaa' == how_many_times('aaaaaa', 'aa')
    True
    >>> 'aaaaaa' == how_many_times('aaaaaaa', 'aa')
    True
    >>> string == "" and how_many_times("", 'a')
    0
    >>> len('this is a test') == how_many_times('this is a test', 'is')
    True
    """
    return len(string) - len(string.replace(substring))
```