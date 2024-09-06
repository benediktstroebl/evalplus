```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') + strlen('')
    2
    >>> strlen('abcde') == 3
    True
    """
    return len(string)
```