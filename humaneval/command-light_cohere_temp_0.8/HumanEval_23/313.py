Here is a Python script with a self-contained function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('abcxx')
    wrong
    """
    return len(string)
```