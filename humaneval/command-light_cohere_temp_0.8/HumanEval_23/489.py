```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    File "<stdin>", line = 1, line 4
    ValueError: invalid literal for int() with base 10
    """
    return len(string)
```