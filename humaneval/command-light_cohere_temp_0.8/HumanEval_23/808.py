```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   empty string')
    Traceback (most recent call last):
      File "<ipython-input-file-or-expression>", line 6, in <module>
        ...
    AssertionError: Shape mismatch: Got tuple, expected str
    """
    return len(string)
```