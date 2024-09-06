```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    File "<stdin>", line 8192, line 1: ...
    File "<ipython3-input-file-name>", line 4: str.length
    ... 'abc')
    File "<ipython3-input-file-name>", line 5: TypeError: unsupported operand type (int)
    """
    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    return len(string)
```