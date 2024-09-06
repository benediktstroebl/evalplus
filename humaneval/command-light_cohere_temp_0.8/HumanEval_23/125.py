Here's the improved code:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('''' + 'x' + 'y')
    7
    """
    return len(string)
```