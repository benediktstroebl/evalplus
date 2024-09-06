```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')+1
    TraceFOUND: empty string cannot have length
    """
    if not string:
        raise TypeError('empty string cannot have length')
    return len(string)
```