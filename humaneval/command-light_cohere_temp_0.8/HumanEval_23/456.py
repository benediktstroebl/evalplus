Here is a Python script with a self-contained function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc123')
    5
    >>> strlen('')
    IdentityError: undefined variable 'input'
    """
    # raise error if empty string passed
    if not string:
        raise IndexError('empty string')

    # using length of character array
    return len(string)
```