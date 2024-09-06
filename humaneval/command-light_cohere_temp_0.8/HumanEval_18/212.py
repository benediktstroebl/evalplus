```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    >>> string = 'aaaaaaa'
    >>> how_many_times(string, 'a')
    3
    >>> string = 'awocowaraowaroowaraow'
    >>> how_many_times(string, 'o')
    3
    >>> string = 'ab cd ef gf hj'
    >>> how_many_times(string, 'g')
    2
    >>> string = 'abcdeffgg'
    >>> how_many_times(string, 'ef')
    3
    """
    count = 0
    sub = substring
    res = []
    for i in string:
        if sub in i:
            count += 1
        res.append(count)
    return res
    return 0
```