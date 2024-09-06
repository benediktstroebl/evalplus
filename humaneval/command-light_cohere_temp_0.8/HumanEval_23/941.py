Here's the self-contained Python function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('ello world')
    5
    >>> strlen('') == 0
    True
    """
    return len(string)
```