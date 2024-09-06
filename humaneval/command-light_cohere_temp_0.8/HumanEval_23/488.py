```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') != 0
    False
    >>> 'x' * strlen('x') == len('xxx')
    True
    >>> 'a' + strlen('a') == len('aa')
    True
    """
    return len(string)
```