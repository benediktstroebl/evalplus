```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')+1
    Traceback (most recent call last):
      File "<ipython file>", line 1, in strlen
    TypeError: 'str' object does not support item assignment
    """
    return len(string)
```