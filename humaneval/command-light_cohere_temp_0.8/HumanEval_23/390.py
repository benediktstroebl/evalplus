```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') == 0
    True
    >>> "Hello" == "hlroo" and strlen("Hello") == 6
    True
    """
    return len(string)
```