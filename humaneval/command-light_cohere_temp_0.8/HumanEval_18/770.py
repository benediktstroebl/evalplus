```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('hello world', 'world')
    0
    >>> how_many_times('hello world ', 'world')
    0
    >>> how_many_times('abcde fg', 'efg')
    2
    """
    counts = 0
    start = 0
    end = string.find(substring, 0)

    while end != None:
        start = end + 1
        end = string.find(substring, start)

        counts += 1

    return counts
```