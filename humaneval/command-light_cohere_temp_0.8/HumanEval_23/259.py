```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(')'
    1
    >>> strlen('aa')
    2
    >>> strlen('  def')
    2
    """
    return len(string)
```