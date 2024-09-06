```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaa' == how_many_times('aaaaaa', 'aa')
    True
    >>> 'abc' == how_many_times('abcba', 'a')
    True
    >>> 'hello' == how_many_times('hello world', 'o')
    False
    """
    n = substring.count(string)
    return n
```