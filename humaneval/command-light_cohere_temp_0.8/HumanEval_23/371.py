```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abc') == 3
        True
        >>> 'hello' == len('hello')
        True
        >>> 'hello' == len('otherapist')
        False
    """
    return len(string)
```