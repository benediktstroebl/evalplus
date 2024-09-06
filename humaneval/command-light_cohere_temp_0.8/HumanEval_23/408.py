```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('hello world')
    11
    >>> strlen('') == 0
    True
    >>> len('') > strlen('')
    True
    """
    return len(string)
```