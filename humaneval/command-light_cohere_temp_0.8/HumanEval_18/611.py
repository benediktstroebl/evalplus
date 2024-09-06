Here is a Python script that defines a function to solve the problem of counting the frequency of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string. 
    Counting overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```