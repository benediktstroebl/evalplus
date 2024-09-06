```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<filename>", line 10, in <module>
        strlen('')
    ZeroDivisionError: division by zero
    """
    return len(string)
```