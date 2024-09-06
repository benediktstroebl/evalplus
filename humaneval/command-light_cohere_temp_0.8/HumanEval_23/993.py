Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('aa')
    2
    >>> strlen('')
    0
    >>> len('hellothere')
    10
    """
    return len(string)
```