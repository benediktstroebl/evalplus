```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<filename>", line 9, in strlen
        raise ValueError('empty string')
    """
    if not string:
        raise ValueError('empty string')
    return len(string)
```