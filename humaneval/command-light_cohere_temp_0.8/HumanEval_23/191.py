```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
    ...
    ValueError: 'abc' not alphabetically sorted
    """
    return sum(1 for c in string if c.isalpha())

```