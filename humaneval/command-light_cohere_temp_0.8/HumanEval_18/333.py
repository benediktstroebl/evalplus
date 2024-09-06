```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('abcda', 'abc')
    3 
    >>> how_many_times('abcddada', 'abc')
    0 
    >>> how_many_times('hello world ', 'world')
    2 
    >>> how_many_times('aa bbb ccc', 'b')
    3 
    >>> how_many_times('aa', 'a')
    0 
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```