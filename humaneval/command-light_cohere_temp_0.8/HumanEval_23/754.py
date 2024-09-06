```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('hello world')
    9
    >>> lengths = ['', 'abc', '123']
    [len(s) for s in lengths]
    """
    return len(string)
```