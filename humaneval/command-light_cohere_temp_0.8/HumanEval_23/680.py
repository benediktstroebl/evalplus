```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<input>", line 1, in strlen
        ValueError: 'argument' must be str, not None
    """
    if not str(string):
        raise ValueError("'argument' must be str, not None")
    return len(string)
```