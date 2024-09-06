```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    TracepleaseError: Cannot instantiate str with an integer
    """
    return len(string)
```