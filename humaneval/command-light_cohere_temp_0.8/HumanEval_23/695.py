Here is a Python script that contains a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') == 0
    True
    >>> len('') == strlen('')
    True
    """
    return len(string)
```