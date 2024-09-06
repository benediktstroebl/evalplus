Here is a self-contained Python script that defines a function to solve the problem of counting the frequency of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    6
    """
    return len([x == substring for x in string])
```