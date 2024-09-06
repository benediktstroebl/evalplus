Here is a Python script that contains a self-contained function that solves the problem of getting the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<filename>", line 1, in <module>
        return 0
    AssertionError: '' not iterable
    """
    return len(string)
```