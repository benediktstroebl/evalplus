Here is a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('Spaces are for )')
    5
    >>> strlen('') == 0
    True
    """
    return len(string)
```