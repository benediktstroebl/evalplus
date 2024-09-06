```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc abc')
    4
    >>> strlen('') | None
    Traceback (most recent call last):
      File "<filename>", line 5, in strlen
        raise TypeError
    """
    if not string:  # check for None input
        raise TypeError("Input cannot be None")
    return len(string)
```