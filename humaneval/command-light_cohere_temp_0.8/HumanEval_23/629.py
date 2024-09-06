Here is a self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen('ℯ')
    3
    >>> strlen('html')
    5
    >>> strlen(' dominoes')
    6
    """
    return len(string)
```