```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    0
    >>> 'hello world' * 10 > strlen('hello world')
    True
    """
    return len(string)
```