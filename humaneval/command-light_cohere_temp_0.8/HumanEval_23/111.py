```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('      ')
    4
    >>> strlen('python')==len('python')
    True
    """
    return len(string)
```