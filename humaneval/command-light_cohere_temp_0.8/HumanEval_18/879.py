```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of first occurrences of the substring in the string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    0
    >>> how_many_times('hello world', 'world')
    0
    >>> how_many_times('aa1234', '1234')
    2
    """
    count = 0
    start = 0
    for i, char in enumerate(string):
        if char == substring:
            start = i+1
        if start == len(string):
            count = i+1
        if count == 0:
            break
    return count
```