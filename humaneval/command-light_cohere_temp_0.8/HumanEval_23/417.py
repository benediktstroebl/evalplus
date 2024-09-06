```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') == 0
    True
    >>> 'hi' == strlen('hi')
    True
    >>> '''a
    b
    c'''' == strlen('abc')
    True
    """
    return len(string)
```