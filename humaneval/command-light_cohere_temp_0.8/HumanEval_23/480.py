Here's the self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   )
    0
    >>> strlen(' '''')
    4
    >>> strlen('A')
    1
    >>> strlen('A  ')
    1
    >>> strlen('foo bar')
    7
    """
    return len(string)
```