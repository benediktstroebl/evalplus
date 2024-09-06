Here is a self-contained Python script that solves the problem of finding the number of times a substring can be found in the original string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('123456', '123')
    4
    >>> how_many_times(' WingCoder', 'Coder')
    2
    """
    count = 0
    for i in string:
        if i == substring:
            count += 1
    return count
```