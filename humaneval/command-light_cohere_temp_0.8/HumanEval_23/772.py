Certainly, here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   )
    5
    >>> strlen('uddled')
    6
    """
    return len(string)
```