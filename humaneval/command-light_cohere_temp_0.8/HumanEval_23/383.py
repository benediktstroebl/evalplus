```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> len('Hello World')
    13
    >>> 'This is a long string'*.len()
    34
    """
    return len(string)
```