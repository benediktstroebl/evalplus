Certainly! Here's the Python script with a self-contained function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abc''')
    0
    >>> strlen('    ')
    3
    >>> strlen('  ')
    2
    >>> strlen('   W')
    3
    >>> strlen('   w#')
    2
    """
    return len(string)
```