```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen(' ')
    1
    >>> strlen('   xyzbcx')
    3
    >>> len('') < strlen('')
    True
    >>> ''.join()
    Traceback (None, None): File "<stdin>", line 30,cell range 41
    File "<stdin>", line 2, line 3
    AssertionError: ''.join() longer than 0 character
    """
    return len(string)
```