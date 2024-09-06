Here's a self-contained Python script with a function `strlen()` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen(')'')
    0
    >>> strlen('icking')
    4
    """
    return len(string)
```